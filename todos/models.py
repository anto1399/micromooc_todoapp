# Importing Dependencies
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# ToDo class with attributes definition. creator (User who created todos), status with one choices at active or completed


class Todo(models.Model):
    TODO_STATUS = (
        ('active', 'Active'),
        ('completed', 'Done')
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
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
