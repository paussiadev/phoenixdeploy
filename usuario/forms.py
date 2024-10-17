from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'cpf', 'profile_picture', 'idioma']