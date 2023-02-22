from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm

class RegisterForm(UserCreationForm):
    
    username = forms.CharField(label="Nom d'utilisateur")
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Prénom")
    last_name = forms.CharField(label="Nom")
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput,
                                help_text="Le mot de passe doit contenir au moins 8 caractères, dont au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial.")
    password2 = forms.CharField(label="Confirmer le mot de passe", widget=forms.PasswordInput, 
                                help_text="Veuillez entrer le même mot de passe que ci-dessus, pour vérification.")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de Passe", widget=forms.PasswordInput)
    
    error_messages = {
        'invalid_login': "Veuillez rentrer un nom d'utilisateur ou un mot de passe valide pour vous connectez.",
        'inactive': "Le compte est inactif ou n'a pas été créer.",
    }
    
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))