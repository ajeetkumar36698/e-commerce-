from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class CustomerRegistionForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'ipt '}))
    password2=forms.CharField(label='Conform Password',widget=forms.PasswordInput(attrs={'class':'ipt '}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'ipt '}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'ipt'})}

class loginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'atuofocus':True,'class':'ipt '}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'attocomplate':'current_password','class':'ipt '}))



class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True,  'class':'ipt login'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'ipt login'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'ipt login'}))
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'ipt login'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'ipt login'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'ipt login'}))
class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['name', 'locality', 'city', 'state', 'zipcode']
    widgets = {'name':forms.TextInput(attrs={'class':'ipt login'}),'locality':forms.TextInput(attrs={'class':'ipt login'}), 'city':forms.TextInput(attrs={'class':'ipt login'}), 
    'state':forms.Select(attrs={'class':'ipt login'}),
    'zipcode':forms.NumberInput(attrs={'class':'ipt login'})}