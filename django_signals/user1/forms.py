from django import forms
from .models import User, Store

class UserForm(forms.ModelForm):
    name = forms.CharField()
    logo = forms.ImageField()
    description = forms.CharField()

    class Meta:
        model = User
        fields = ('name', 'logo', 'description')
        
class StoreForm(forms.ModelForm):
    # name = models.CharField(max_length=30)    
    # address = models.CharField(max_length=30,unique=True)
    # city = models.CharField(max_length=30)
    # state = models.CharField(max_length=2)
    class Meta:
        model = Store
        fields = ('name', 'address', 'city', 'state')