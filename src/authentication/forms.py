from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")
        
class SingupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]
        
class EditInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "photo_profile",
        ]
        labels = {
            "username": "Nom d'utilisateur",
            "email": "Addresse email", 
            "first_name": "Prénom", 
            "last_name": "Nom", 
        }
