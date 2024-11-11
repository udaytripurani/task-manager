


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

#### Curl Command:

```bash
curl -X POST http://localhost:8000/api-token-auth/ \
     -H "Content-Type: application/json" \
     -d '{"username": "yourusername", "password": "yourpassword"}'
```

- **Request Body**: 
  ```json
  {
    "username": "yourusername",
    "password": "yourpassword"
  }
  ```

- **Response**: 
  ```json
  {
    "token": "your_token_here"
  }
  ```

### **Task Management Endpoints**

#### 1. `GET /api/tasks/`: List all tasks.

#### Curl Command:

```bash
curl -X GET http://localhost:8000/api/tasks/ \
     -H "Authorization: Token <your_token>"
```

#### 2. `POST /api/tasks/`: Create a new task.

#### Curl Command:

```bash
curl -X POST http://localhost:8000/api/tasks/ \
     -H "Authorization: Token <your_token>" \
     -H "Content-Type: application/json" \
     -d '{"title": "Task Title", "description": "Task Description", "completed": false}'
```

- **Request Body**:
  ```json
  {
    "title": "Task Title",
    "description": "Task Description",
    "completed": false
  }
  ```

#### 3. `GET /api/tasks/{id}/`: Retrieve a specific task by ID.

#### Curl Command:

```bash
curl -X GET http://localhost:8000/api/tasks/1/ \
     -H "Authorization: Token <your_token>"
```

#### 4. `PUT /api/tasks/{id}/`: Update a task by ID.

#### Curl Command:

```bash
curl -X PUT http://localhost:8000/api/tasks/1/ \
     -H "Authorization: Token <your_token>" \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Task", "description": "Updated Description", "completed": true}'
```

- **Request Body**:
  ```json
  {
    "title": "Updated Task",
    "description": "Updated Description",
    "completed": true
  }
  ```

#### 5. `DELETE /api/tasks/{id}/`: Delete a task by ID.

#### Curl Command:

```bash
curl -X DELETE http://localhost:8000/api/tasks/1/ \
     -H "Authorization: Token <your_token>"
```

### **Filtering and Pagination**

You can filter tasks using query parameters:
- `completed=true/false`: Filter tasks by completion status.
- `created_after={date}`: Filter tasks created after a specific date.
- `updated_after={date}`: Filter tasks updated after a specific date.

#### Example Curl Command for Filtering:

```bash
curl -X GET "http://localhost:8000/api/tasks/?completed=true" \
     -H "Authorization: Token <your_token>"
```

Pagination is applied by default with 10 tasks per page.

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

---


