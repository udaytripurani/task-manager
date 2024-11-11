from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow read-only access to non-authenticated users,
    while ensuring that only admin users can perform write operations (POST, PUT, DELETE).
    """
    
    def has_permission(self, request, view):
        """
        Check if the user has permission to perform the requested operation.
        
        Args:
            request (Request): The request object containing user and method information.
            view (View): The view object being accessed.

        Returns:
            bool: True if the request is allowed, False otherwise.
        """
        # Allow access to authenticated users with staff privileges (admin users) for all methods
        if request.user.is_staff:
            return True
        
        # Allow read-only methods (GET, HEAD, OPTIONS) to be accessed by any user
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        
        # Deny access for non-admin users trying to perform write operations
        return False
    
    # tasks/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins to modify objects.
    Non-admins can only create their own tasks and view tasks.
    """
    
    def has_permission(self, request, view):
        # Allow any GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow authenticated users to create tasks (POST requests)
        if request.method == 'POST':
            return request.user and request.user.is_authenticated

        # Allow write permissions only if the user is an admin
        return request.user and request.user.is_staff

