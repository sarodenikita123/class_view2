from django import forms
from .models import Bank


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = "__all__"

        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "customer_last_name": forms.TextInput(attrs={"class": "form-control"}),
            "customer_account_no": forms.TextInput(attrs={"class": "form-control"}),
            "bank_branch": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput()

        }
