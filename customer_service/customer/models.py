# customers/models.py

from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    customer_id = models.AutoField(primary_key=True)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            last_customer = Customer.objects.order_by('customer_id').last()
            if last_customer:
                self.customer_id = last_customer.customer_id + 1
            else:
                self.customer_id = 100000000  # Starting sequence number
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

