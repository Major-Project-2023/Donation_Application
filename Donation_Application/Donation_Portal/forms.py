from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField,PasswordResetForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer
from paypal.standard.forms import PayPalPaymentsForm

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = '__all__'
        fields = ['phone','address','country','ac_number', 'ifsc_code']
        widgets = {'phone':forms.NumberInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'country':forms.TextInput(attrs={'class':'form-control'}),
        'ac_number':forms.NumberInput(attrs={'class':'form-control'}),
        'ifsc_code':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Enter registered email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
    )

class DonationForm(forms.Form):
    amount=forms.DecimalField(label='Donation Amount')
# class CustomPayPalPaymentsForm(PayPalPaymentsForm):

#     def get_html_submit_element(self):
#         return """<button type="submit">Continue on PayPal website</button>"""
        
        # BUY = "buy"
        # SUBSCRIBE = "subscribe"
        # DONATE = "donate"
        # PAY = "pay"
        # def get_image(self):
        #     return {
        #     self.SUBSCRIBE: SUBSCRIPTION_BUTTON_IMAGE,
        #     self.BUY: BUY_BUTTON_IMAGE,
        #     self.DONATE: DONATION_BUTTON_IMAGE,
        #     self.PAY: PAY_BUTTON_IMAGE,
        #     }[self.button_type]

        # def is_donation(self):
        #     warn_untested()
        #     return self.button_type == self.DONATE
