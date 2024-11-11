from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task
from rest_framework.authtoken.models import Token

class TaskAPITests(APITestCase):
    def setUp(self):
        """
        Set up the test environment by creating users, tasks, and authentication tokens.
        """
        # Create two users: one admin and one regular user
        self.admin_user = User.objects.create_user(username="admin", password="password", is_staff=True)
        self.regular_user = User.objects.create_user(username="regular_user", password="password")
        
        # Create tasks for both users
        self.task_admin = Task.objects.create(title="Admin's Task", description="Task created by admin", user=self.admin_user)
        self.task_regular_user = Task.objects.create(title="Regular User's Task", description="Task created by regular user", user=self.regular_user)
        
        # Generate tokens for both users
        self.admin_token = Token.objects.create(user=self.admin_user)
        self.regular_user_token = Token.objects.create(user=self.regular_user)

    def test_create_task_by_authenticated_user(self):
        """
        Verify that authenticated users can create a task.
        """
        # Authenticate with regular user token
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.regular_user_token.key}')
        
        # Define data for the new task
        task_data = {
            "title": "New Task",
            "description": "Task created by regular user"
        }
        
        # Make a POST request to create a new task
        response = self.client.post('/api/tasks/', task_data, format='json')
        
        # Assert that the response status is HTTP_201_CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify that the task has been created and assigned to the regular user
        task = Task.objects.get(id=response.data['id'])
        self.assertEqual(task.user, self.regular_user)
        self.assertEqual(task.title, task_data['title'])
        self.assertEqual(task.description, task_data['description'])

    def test_admin_access_to_all_tasks(self):
        """
        Verify that admin users can access all tasks.
        """
        # Authenticate with admin token
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        
        # Get all tasks
        response = self.client.get('/api/tasks/')
        
        # Assert that the response status is OK (200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that the admin user can see both tasks (admin and regular user's tasks)
        task_titles = [task['title'] for task in response.data['results']]
        self.assertIn(self.task_admin.title, task_titles)
        self.assertIn(self.task_regular_user.title, task_titles)

    def test_regular_user_access_to_own_tasks(self):
        """
        Verify that regular users can only access their own tasks.
        """
        # Authenticate with regular user token
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.regular_user_token.key}')
        
        # Get tasks for the regular user
        response = self.client.get('/api/tasks/')
        
        # Assert that the response status is OK (200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that the regular user can see only their own task
        task_titles = [task['title'] for task in response.data['results']]
        self.assertIn(self.task_regular_user.title, task_titles)
        self.assertNotIn(self.task_admin.title, task_titles)
