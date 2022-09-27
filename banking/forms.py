
from pyexpat import model
from django import forms
from banking.models import Accholder, Transactions


class CreateAccountForm(forms.ModelForm):
    '''
    For creating Bank Account
    '''

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
    '''
    For making deposit or withdraw
    '''
    class Meta:
        model = Transactions
        fields= ['t_type','amount']

        widgets={
                't_type': forms.Select(attrs={'class':'form-control','placeholder':"Transaction Type"}),
                'amount':forms.TextInput(attrs={'class':'form-control','placeholder':"Amount"})
            }

class TransferForm(forms.ModelForm):
    '''
    For transfering Money
    '''
    class Meta:
        model = Transactions
        fields= ['reciver','amount']

        widgets={
                'reciver': forms.TextInput(attrs={'class':'form-control','placeholder':"Reciver"}),
                'amount':forms.TextInput(attrs={'class':'form-control','placeholder':"Amount"})
            }