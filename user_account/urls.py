# Import the Needed Dependencies
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
# Login and Registration URLs
#path('login/', views.user_login, name='login'),
path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('register/', views.register, name='register'),

# Dashboard and other pages to show your todos
path('', views.dashboard, name='dashboard'),
path('/active', views.active_todos, name='active_todos'),
path('completed', views.completed_todos, name='completed_todos'),

# change password URLs
path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]