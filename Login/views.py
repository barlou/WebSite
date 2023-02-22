from django.shortcuts import render, redirect 
from Login.form import RegisterForm, CustomAuthenticationForm, CustomPasswordResetForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed:feed-home')
    else: 
        form = RegisterForm()
    return render(request, 'Login/templates/signin.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home:Home-index')  # replace 'home' with the name of your home view
    else:
        form = CustomAuthenticationForm()

    return render(request, 'Login/templates/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('feed:feed-home')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'Login/templates/password_reset.html'
    email_template_name = 'Login/templates/password_reset_email.html'
    form_class = CustomPasswordResetForm

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'Login/templates/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'Login/templates/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'Login/templates/password_reset_complete.html'
