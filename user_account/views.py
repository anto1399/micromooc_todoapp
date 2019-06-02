# Importing Dependencies

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from todos.models import Todo, CompletedTodosManager, ActiveTodosManager
from django.views.generic.edit import CreateView


# User Login Action

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Authenticate the user and redirect to the dashboard
            user = authenticate(request,
                    username=cd['username'],
                    password=cd['password'])
            if user is not None:    
                if user.is_active:
                    login(request, user)
                    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
                else:
                    messages.error(request, 'Account is Disabled')
            else:
                messages.error(request, 'Invalid Login Details')   
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
                    messages.success(request, 'You have successfuly created a new account, Begin creating your TODOs')
                    return render(request, 'account/dashboard.html', {'section': 'dashboard'})         
    else:
        # Send the Registration form to user to enter login credentials for GET http request
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# Check if user is authenticated before sending to dashboard, else show login page
@login_required

# User is directed to dashboard after successful login, together with his ToDos items
def dashboard(request):
    # Get All Todos Associated with the Authenticated User
    all_user_todos = Todo.todos.filter(creator=request.user)
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'my_todos': all_user_todos})


#Get all ACTIVE todos of the authenticated user
@login_required
def active_todos(request):
    # Get All Todos Associated with the Authenticated User
    active_user_todos = Todo.active.filter(creator=request.user)
    return render(request, 'account/active_todos.html', {'section': 'active', 'active_todos': active_user_todos})


#Get all COMPLETED todos of the authenticated user
@login_required
def completed_todos(request):
    # Get All Todos Associated with the Authenticated User
    completed_user_todos = Todo.completed.filter(creator=request.user)
    return render(request, 'account/completed_todos.html', {'section': 'completed', 'completed_todos': completed_user_todos})


# Get a single todo details
@login_required
def todo_details(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'account/todo_details.html', {'todo': todo})