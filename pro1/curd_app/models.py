from django.db import models


class Bank(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=20)
    customer_account_no = models.CharField(max_length=20)
    bank_branch = models.CharField(max_length=20)
    amount = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

