
from pyexpat import model
from django import forms
from banking.models import Accholder, Transactions


"""
This class is used to create a form for the Transactions model.
this contians the fields that are required for the Transactions model like the account_number and the amount
"""
class CreateAccountForm(forms.ModelForm):

    class Meta:
        model = Accholder
        fields = ['user','name','email','acc_type','pan', 'aadhaar']
        # fields = '__all__'

        widgets={
    
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':"Name"}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':"Email"}),
            'acc_type':forms.Select(attrs={'class':'form-control','placeholder':"Account_Type"}),
            'pan':forms.TextInput(attrs={'class':'form-control','placeholder':"Pan"}),
            'aadhaar':forms.TextInput(attrs={'class':'form-control','placeholder':"Aaadhaar"}),
        }




class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields= ['t_type','amount']

        widgets={
                't_type': forms.Select(attrs={'class':'form-control','placeholder':"Transaction Type"}),
                'amount':forms.TextInput(attrs={'class':'form-control','placeholder':"Amount"})
            }

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields= ['reciver','amount']

        widgets={
                'reciver': forms.TextInput(attrs={'class':'form-control','placeholder':"Reciver"}),
                'amount':forms.TextInput(attrs={'class':'form-control','placeholder':"Amount"})
            }