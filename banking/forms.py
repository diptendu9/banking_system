
from django import forms
from banking.models import Accholder


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

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
