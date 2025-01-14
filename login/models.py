from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)  # Title of the task
    description = models.TextField(blank=True, null=True)  # Optional detailed description
    completed = models.BooleanField(default=False)  # Completion status of the task
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the task was created
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the user who owns the task

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed']
         
