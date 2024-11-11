

# Task Management API

A simple Task Management API built using Django and Django Rest Framework. This API allows users to manage tasks with CRUD operations, apply filters to tasks, and handle authentication via tokens. It includes role-based access control, allowing only authenticated users to manage their own tasks, while admin users can access and manage all tasks.

## Features

- **User Authentication**: Token-based authentication using Django Rest Framework's `TokenAuthentication` or `JWTAuthentication`.
- **CRUD Operations**: 
  - Create a new task.
  - List all tasks.
  - Get task details.
  - Update a task.
  - Delete a task.
- **Permissions**:
  - Only authenticated users can create, update, or delete tasks.
  - Admin users can view and manage all tasks.
  - Users can only access their own tasks.
- **Task Filtering**: Filter tasks by completion status, created date, or updated date.
- **Pagination**: Task lists are paginated, displaying a maximum of 10 tasks per page.
- **Error Handling**: Proper error responses for invalid requests.

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django Rest Framework (DRF)**: A powerful toolkit for building Web APIs in Django.
- **SQLite (default)**: Default database for local development (can be switched to PostgreSQL, MySQL, etc.).
- **Token Authentication**: DRF's TokenAuthentication or JWT for securing API endpoints.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/task-management-api.git
    cd task-management-api
    ```

2. **Create and Activate Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate   # For Windows, use venv\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser** (Optional for Admin Access):

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

    The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

### **Authentication Endpoints**

- `POST /api-token-auth/`: Obtain a token for authentication.
  - **Request Body**: `{ "username": "yourusername", "password": "yourpassword" }`
  - **Response**: `{ "token": "your_token_here" }`

### **Task Management Endpoints**

- `GET /api/tasks/`: List all tasks.
- `POST /api/tasks/`: Create a new task.
  - **Request Body**: `{ "title": "Task Title", "description": "Task Description", "completed": false }`
- `GET /api/tasks/{id}/`: Retrieve a specific task by ID.
- `PUT /api/tasks/{id}/`: Update a task by ID.
  - **Request Body**: `{ "title": "Updated Task", "description": "Updated Description", "completed": true }`
- `DELETE /api/tasks/{id}/`: Delete a task by ID.

### **Filtering and Pagination**

- You can filter tasks using query parameters:
  - `completed=true/false`: Filter tasks by completion status.
  - `created_after={date}`: Filter tasks created after a specific date.
  - `updated_after={date}`: Filter tasks updated after a specific date.

- Pagination is applied by default with 10 tasks per page.

## Permissions

- **Admin Users**: Admin users can access and manage all tasks in the system.
- **Authenticated Users**: Only authenticated users can create, update, or delete tasks. Users can only interact with their own tasks.
- **Non-Authenticated Users**: Cannot create, update, or delete tasks but can view the list of tasks.

## Running Tests

To run the tests, use Django's built-in testing framework or `pytest`:

1. **Run Django Tests**:

    ```bash
    python manage.py test
    ```

2. **Run Tests with pytest**:

    ```bash
    pytest
    ```

