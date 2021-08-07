from django import forms
from django.forms import fields
from django.forms.widgets import PasswordInput

class postform(forms.Form):
    name=forms.CharField(label='Name',label_suffix=' ',widget=forms.TextInput(attrs={'id':'nameid','class':'form-control','placeholder':'user'}))
    email=forms.EmailField(label='Email',label_suffix=' ',widget=forms.EmailInput(attrs={'id':'emailid','class':'form-control','placeholder':'user@gmail.com'}))
    password=forms.CharField(label='Password',label_suffix=' ',widget=forms.PasswordInput(attrs={'id':'passwordid','class':'form-control','placeholder':'user1234'}))

    class Meta:
        fields=['name','email','password']