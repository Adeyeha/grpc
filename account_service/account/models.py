# accounts/models.py

from django.db import models

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('Savings', 'Savings'),
        ('Checking', 'Checking'),
    ]

    CURRENCIES = [
        ('USD', 'USD'),
        ('GBP', 'GBP'),
        ('EUR', 'EUR'),
        ('CAD', 'CAD'),
    ]

    account_number = models.AutoField(primary_key=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    currency = models.CharField(max_length=3, choices=CURRENCIES)
    customer_id = models.CharField(max_length=9)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)

    class Meta:
        unique_together = ['customer_id', 'account_type', 'currency']

    def save(self, *args, **kwargs):
        if not self.account_number:
            last_account = Account.objects.order_by('account_number').last()
            if last_account:
                self.account_number = str(int(last_account.account_number) + 1)
            else:
                self.account_number = '1000000000'  # Starting sequence number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account_number
