# Importing Dependencies
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# User Login Action
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                    username=cd['username'],
                    password=cd['password'])
            if user is not None:    
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        # Send the login form to user to enter login credentials for GET http request
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


# User Registration Action
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Authenticate the user and redirect to the dashboard
            user = authenticate(request,
                    username=user_form.cleaned_data['username'],
                    password=user_form.cleaned_data['password'])
            if user is not None:    
                if user.is_active:
                    login(request, user)
                    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')              
    else:
        # Send the Registration form to user to enter login credentials for GET http request
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# User is directed to dashboard after successful login, "section" is used to check the page of the auth user
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})