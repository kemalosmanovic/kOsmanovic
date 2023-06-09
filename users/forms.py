from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =['username', 'email', 'first_name', 'last_name',  'password1', 'password2']
     
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']  
   

class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField()
    class Meta:
        model = Profile
        fields = ['image', 'date_of_birth', 'address', 'city_or_town', 'country']


