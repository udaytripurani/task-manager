from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Task model that represents a to-do item or task in the system.
    
    Fields:
        title (CharField): The title of the task.
        description (TextField): Detailed description of the task.
        completed (BooleanField): Status of task completion (default is False).
        created_at (DateTimeField): Timestamp of task creation, set automatically.
        updated_at (DateTimeField): Timestamp of last update, set automatically.
        user (ForeignKey): Reference to the user who created the task; 
                           tasks are deleted if the user is removed.
    """

    title = models.CharField(max_length=255, help_text="The title or name of the task.")
    description = models.TextField(help_text="A detailed description of the task.")
    completed = models.BooleanField(default=False, help_text="Indicates whether the task is completed.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the task was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the task was last updated.")
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="tasks",
        help_text="The user who owns this task."
    )

    def __str__(self):
        """Returns a string representation of the task, which is the title."""
        return self.title

    class Meta:
        ordering = ['-created_at']  # Orders tasks by creation date in descending order by default
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
