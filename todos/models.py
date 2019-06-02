# Importing Dependencies
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# ToDo class with attributes definition. creator (User who created todos), status with one choices at active or completed

# All Active Todos for an authenticated user
class ActiveTodosManager(models.Manager):
    def get_queryset(self):
        return super(ActiveTodosManager, self).get_queryset().filter(status='active')

# All Completed Todos for an authenticated user
class CompletedTodosManager(models.Manager):
    def get_queryset(self):
        return super(CompletedTodosManager, self).get_queryset().filter(status='completed')



class Todo(models.Model):
    # manager APIs For Interacting with Todos
    todos = models.Manager()
    active = ActiveTodosManager()
    completed = CompletedTodosManager()

    
    # Todo Schema definition
    TODO_STATUS = (
        ('active', 'Active'),
        ('completed', 'Done')
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todos_creates')
    status = models.CharField(
        max_length=10, choices=TODO_STATUS, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


# Default orderBy descending order of magnitude with -ve created_at

    class Meta:
        ordering = ('-created_at',)

# Human Readable representation of returned todos object
    def __str__(self):
        return self.title

# Utility for refrencing the Todo object in the URL template name
    def get_absolute_url(self): # new
        return reverse('todo_details', args=[str(self.id)])