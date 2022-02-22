from django import forms
from django.core.exceptions import ValidationError

from .models import UserProfile
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .validators import validate_domainonly_email

# another python package
# from captcha.fields import CaptchaField

class UserProfileForm(forms.ModelForm):
    mobile_no = forms.CharField()
    address = forms.CharField(widget=forms.Textarea())
    # dob = forms.DateField()
    user_pic = forms.ImageField()
    
    class Meta:
        model = UserProfile
        fields = ('staff', 'mobile_no', 'address', 'user_pic')


class RegisterNewUser(UserCreationForm):
    error_css_class = "error"
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-info'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-info'}))
    # dob = forms.DateField(widget = NumberInput(attrs={'type':'date'}))
    user_pic = forms.ImageField()
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    # confirm_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm Password')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','mobile_no', 'address', 'user_pic', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control text-info',
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control text-info',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control text-info',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control text-info',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control text-info', 
            }),
        }
        labels = {
            'email': 'Email',
            'password1': 'Password'
        }
    
    def clean(self):
        super(RegisterNewUser, self).clean()

        # getting username and password from cleaned_data
        username = self.cleaned_data.get('username')
        mobile_no = self.cleaned_data.get('mobile_no')
        email = self.cleaned_data.get('email')
        # password = self.cleaned_data.get('password')
        # confirm_password = self.cleaned_data.get('confirm_password')

        # here we check the first-character of username.
        if username[0] != '@':
            self._errors['username'] = self.error_class(['A First character of username must be @'])
        
        if len(mobile_no) < 10:
            self._errors['mobile_no'] = self.error_class(['Mobile Number should be 10 digits !!!'])
        
        # if '@gmail.com' not in email:
        #     self._errors['email'] = self.error_class(['Email Address not valid'])

        # if password is not None and password != confirm_password:
        #     self._errors['password'] = self.error_class(['Password and Confirm Password Must be same...'])
        
        return self.cleaned_data


class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'date_joined')
        labels = {
            'email': 'Email'
        }

class EditAdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        