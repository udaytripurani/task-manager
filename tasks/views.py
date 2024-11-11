from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrReadOnly  # Custom permission
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Task model, providing CRUD operations.
    """
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can perform any action

    def perform_create(self, serializer):
        """
        Automatically set the user field to the currently authenticated user when creating a task.
        """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Filter tasks based on the current user. Admin users can see all tasks; regular users only their own.
        """
        if self.request.user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        """
        Override the destroy method to restrict task deletion to the user who created the task.
        """
        task = self.get_object()  # Get the task object to be deleted
        if task.user != request.user:
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Override the update method to restrict task updates to the user who created the task.
        """
        task = self.get_object()
        if task.user != request.user:
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
