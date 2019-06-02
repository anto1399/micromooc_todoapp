from django import forms
from .models import Todo

# Creating Login Forms Class For Todos
class TodoCreateForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        exclude = '__all__'
