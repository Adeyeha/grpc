from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
import json

class ChangeEmailRequest(BaseModel):
    current_phone_number: str
    new_email: str

class ChangePhoneNumberRequest(BaseModel):
    current_phone_number: str
    new_phone_number: str

class CreateAccountExistingCustomer(BaseModel):
    phone_number: str
    currency: str
    account_type: str

class CreateAccountNewCustomer(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    currency: str
    account_type: str 

class CreateTransaction(BaseModel):
    phone_number: str
    amount: float 
    currency: str
    account_type: str 
    dc_ind: str
    description: str

# class GetTransaction(BaseModel):
#     phone_number: str
#     currency: str
#     account_type: str

class CustomerHttpExecption(HTTPException):
    pass

app = FastAPI()

CUSTOMER_API_URL = "http://localhost:8000/api"
ACCOUNT_API_URL = "http://localhost:8001/api"
TRANSACTION_API_URL = "http://localhost:8002/api"

def _get_customer(phone_number):
    try:
        customer_response = requests.get(f"{CUSTOMER_API_URL}/customersbyphone/{phone_number}/")
        customer_response.raise_for_status()  # Raise HTTPError for non-2xx status codes
        customer_data = customer_response.json()
    except requests.RequestException as e:
        error_message = customer_response.json().get('detail')
        if not error_message:
            error_message = customer_response.json()
        raise CustomerHttpExecption(status_code=customer_response.status_code, detail=error_message)
    return customer_data

def _create_account_existing_customer(request_data,customer_id=None):
    # Step 1: Call the customer endpoint with the phone number to get the customer details
    if customer_id is None:
        customer_data = _get_customer(request_data.phone_number)
        customer_id = customer_data.get('customer_id')

    # Step 2: Create a new account for the customer
    try:
        account_data = {
            "customer_id": customer_id,
            "currency": request_data.currency,
            "account_type": request_data.account_type
        }
        create_account_response = requests.post(f"{ACCOUNT_API_URL}/accounts/", data=account_data)
        create_account_response.raise_for_status()  # Raise HTTPError for non-2xx status codes
        created_account_data = create_account_response.json()
    except requests.HTTPError as e:
        error_message = create_account_response.json().get('detail')
        if not error_message:
            error_message = create_account_response.json()
        raise HTTPException(status_code=create_account_response.status_code, detail=error_message)

    return created_account_data

@app.get("/get_accounts/{phone_number}")
def get_accounts(phone_number: str):

    # Step 1: Call the customer endpoint with the phone number

    customer_data = _get_customer(phone_number)
    customer_id = customer_data['customer_id']

    # Step 2: Use the customer ID to call the account endpoint
    try:
        account_response = requests.get(f"{ACCOUNT_API_URL}/accountsbycustomer/{customer_id}/")
        account_response.raise_for_status()  # Raise HTTPError for non-2xx status codes
        accounts = account_response.json()
    except requests.RequestException as e:
        error_message = account_response.json().get('detail')
        if not error_message:
            error_message = account_response.json()
        raise HTTPException(status_code=account_response.status_code, detail=error_message)

    return accounts


@app.put("/change_email")
def change_email(request_data: ChangeEmailRequest):
    # Extract phone number and new email from request data
    phone_number = request_data.current_phone_number
    new_email = request_data.new_email
    
    # Step 1: Call the customer endpoint with the phone number to get the customer details
    customer_data = _get_customer(phone_number)

    # Update the email in the customer data
    customer_data['email'] = new_email

    # Step 2: Use the customer ID to call the customer endpoint with a PUT request to update the customer details
    try:
        update_response = requests.put(f"{CUSTOMER_API_URL}/customersbyphone/{phone_number}/", data=customer_data)
        update_response.raise_for_status()  # Raise HTTPError for non-2xx status codes
        print(update_response)
        updated_customer_data = update_response.json()
    except requests.HTTPError as e:
        error_message = update_response.json().get('detail')
        if not error_message:
            error_message=update_response.json()
        raise HTTPException(status_code=update_response.status_code, detail=error_message)

    return updated_customer_data

@app.put("/change_phone_number")
def change_phone_number(request_data: ChangePhoneNumberRequest):
    # Extract current and new phone numbers from request data
    current_phone_number = request_data.current_phone_number
    new_phone_number = request_data.new_phone_number
    
    # Step 1: Call the customer endpoint with the current phone number to get the customer details
    customer_data = _get_customer(current_phone_number)

    # Update the phone number in the customer data
    customer_data['phone_number'] = new_phone_number

    # Step 2: Use the customer ID to call the customer endpoint with a PUT request to update the customer details
    try:
        update_response = requests.put(f"{CUSTOMER_API_URL}/customersbyphone/{current_phone_number}/", json=customer_data)
        update_response.raise_for_status()  # Raise HTTPError for non-2xx status codes
        updated_customer_data = update_response.json()
    except requests.HTTPError as e:

        error_message = update_response.json().get('detail')
        if not error_message:
            error_message = update_response.json()

        raise HTTPException(status_code=update_response.status_code, detail=error_message)

    return updated_customer_data


@app.post("/create_account_existing_customer")
def create_account_existing_customer(request_data: CreateAccountExistingCustomer):
    return _create_account_existing_customer(request_data)

@app.post("/create_account_new_customer")
def create_account_new_customer(request_data: CreateAccountNewCustomer):
    # Step 1: Call the customer endpoint with the phone number to check if the customer exists
    try:
        customer_data = _get_customer(request_data.phone_number)
        customer_id = customer_data.get('customer_id')

        # Step 2: If the customer exists, call the create_account_existing_customer endpoint
        if customer_id:
            return _create_account_existing_customer(request_data,customer_id=customer_id)
        
    except CustomerHttpExecption as e:
        # Step 3: If the customer doesn't exist, create a new customer
        try:
            new_customer_data = {
                "first_name": request_data.first_name,
                "last_name": request_data.last_name,
                "email": request_data.email,
                "phone_number": request_data.phone_number
            }
            create_customer_response = requests.post(f"{CUSTOMER_API_URL}/customers/", data=new_customer_data)
            create_customer_response.raise_for_status()  # Raise HTTPError for non-2xx status codes
            created_customer_data = create_customer_response.json()
            customer_id = created_customer_data.get('customer_id')

        except requests.HTTPError as e:
            error_message = create_customer_response.json().get('detail')
            if not error_message:
                error_message = create_customer_response.json()

            raise HTTPException(status_code=create_customer_response.status_code, detail=error_message)

    # Step 4: Call the create_account_existing_customer endpoint with the newly created customer's details
    return _create_account_existing_customer(request_data,customer_id=customer_id)


@app.post("/post_transaction")
def post_transaction(request_data: CreateTransaction):
    # Step 1: Call the account endpoint with the retrieved customer ID to get the account details
    accounts = get_accounts(request_data.phone_number)

    filtered_accounts = filter(lambda d: d.get('currency').lower() == request_data.currency.lower() and d.get('account_type') .lower()== request_data.account_type.lower(), accounts)
    filtered_account = next(filtered_accounts, None)

    if filtered_account is None:
        raise HTTPException(status_code=404, detail="No Account matches the given query.")
    
    if float(filtered_account['balance']) < request_data.amount:
        raise HTTPException(status_code=400, detail="Insufficient Balance")

    # Step 2: Post the transaction with the provided amount, currency, and account ID
    try:
        transaction_data = {
            "account": filtered_account.get('account_number'),
            "amount": request_data.amount,
            "currency": request_data.currency,
            "dc_ind": request_data.dc_ind,
            "description": request_data.description,
        }

        post_transaction_response = requests.post(f"{TRANSACTION_API_URL}/transactions/", data=transaction_data)
        post_transaction_response.raise_for_status()  # Raise HTTPError for non-2xx status codes
        posted_transaction_data = post_transaction_response.json()
    except requests.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

    # Step 4: Update the account balance based on the transaction amount and type (credit or debit)
    try:
        if request_data.dc_ind.lower() == 'credit':
            updated_balance = round((float(filtered_account.get('balance')) + request_data.amount),2)
        elif request_data.dc_ind.lower() == 'debit':
            updated_balance = round((float(filtered_account.get('balance')) - request_data.amount),2)
        else:
            raise ValueError("Invalid transaction type")
        filtered_account['balance'] = updated_balance
        update_balance_response = requests.put(f"{ACCOUNT_API_URL}/accounts/{filtered_account.get('account_number')}/", 
                                                data=filtered_account)
        update_balance_response.raise_for_status()  # Raise HTTPError for non-2xx status codes
        updated_account_data = update_balance_response.json()
    except requests.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

    return updated_account_data


@app.get("/get_transaction_history")
def get_transaction_history(phone_number: str, currency: str, account_type: str):
    # Step 1: Call the account endpoint with the retrieved customer ID, currency, and account type to get the account details
    accounts = get_accounts(phone_number)

    filtered_accounts = filter(lambda d: d.get('currency').lower() == currency.lower() and d.get('account_type') .lower()== account_type.lower(), accounts)
    filtered_account = next(filtered_accounts, None)

    if filtered_account is None:
        raise HTTPException(status_code=404, detail="No Account matches the given query.")

    # Step 3: Call the transaction endpoint with the retrieved account ID to get the transaction history
    try:
        transaction_response = requests.get(f"{TRANSACTION_API_URL}/transactionsbyaccount/{filtered_account['account_number']}/")
        transaction_response.raise_for_status()  # Raise HTTPError for non-2xx status codes
        transaction_history = transaction_response.json()
    except requests.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

    return transaction_history
