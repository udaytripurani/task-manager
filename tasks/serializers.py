from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    This serializer is responsible for converting Task instances to JSON format
    and validating the data for creating or updating tasks. It includes fields for
    task details such as title, description, completed status, timestamps, and the 
    user associated with the task.

    Fields:
        - id: Auto-generated ID of the task (read-only).
        - title: The title of the task.
        - description: A detailed description of the task.
        - completed: Boolean indicating whether the task is completed.
        - created_at: Timestamp for when the task was created (read-only).
        - updated_at: Timestamp for when the task was last updated (read-only).
        - user: The user who created the task (read-only).
    """
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at', 'user']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']
        """
        Meta class defines the fields to be serialized and ensures that certain fields
        (id, created_at, updated_at, user) are read-only, meaning they cannot be modified by the client.
        """

    def validate_title(self, value):
        """
        Validate the title field to ensure it is not empty or just whitespace.

        Args:
            value (str): The value of the title field to be validated.

        Returns:
            str: The validated title value.

        Raises:
            ValidationError: If the title is empty or consists of whitespace.
        """
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_completed(self, value):
        """
        Validate the completed field to ensure it is a boolean value (True or False).

        Args:
            value (bool): The value of the completed field to be validated.

        Returns:
            bool: The validated completed value.

        Raises:
            ValidationError: If the completed field is not a boolean.
        """
        if not isinstance(value, bool):
            raise serializers.ValidationError("'completed' must be a boolean value.")
        return value
