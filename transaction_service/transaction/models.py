# transactions/models.py

from django.db import models

class Transaction(models.Model):

    DC_IND_CHOICES = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    dc_ind = models.CharField(max_length=6, choices=DC_IND_CHOICES)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_id} - {self.amount} - {self.currency} - {self.dc_ind}"
