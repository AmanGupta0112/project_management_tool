# Project Management API Documentation

## Overview
This API provides endpoints for managing users, projects, tasks, and comments in a project management tool. It is built using Django REST Framework and is secured with token authentication.

## Base URL
```
http://127.0.0.1:8000/api/
```

## Authentication
All endpoints require authentication. Include a token in the `Authorization` header:
```
Authorization: Token <your_token>
```

## Endpoints

### Users

#### List Users
- **URL:** `/users/`
- **Method:** `GET`
- **Description:** Retrieve a list of all users
- **Response (200 OK):**
  ```json
  [
    {
      "id": 1,
      "username": "user1",
      "email": "user1@example.com"
    }
  ]
  ```

#### Create User
- **URL:** `/users/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "new_user",
    "email": "new_user@example.com",
    "password": "your_password"
  }
  ```
- **Responses:**
  - `201 Created`: Returns the created user
  - `400 Bad Request`: Returns validation errors

#### Retrieve User
- **URL:** `/users/{pk}/`
- **Method:** `GET`
- **Responses:**
  - `200 OK`: Returns user details
  - `404 Not Found`: User does not exist

#### Update User
- **URL:** `/users/{pk}/`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "username": "updated_user",
    "email": "updated_user@example.com"
  }
  ```
- **Responses:**
  - `200 OK`: Returns updated user
  - `400 Bad Request`: Validation errors
  - `404 Not Found`: User does not exist

#### Delete User
- **URL:** `/users/{pk}/`
- **Method:** `DELETE`
- **Responses:**
  - `204 No Content`: Successfully deleted
  - `404 Not Found`: User does not exist

### Projects

#### List Projects
- **URL:** `/projects/`
- **Method:** `GET`
- **Description:** Retrieve all projects
- **Response:** `200 OK`

#### Create Project
- **URL:** `/projects/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "New Project",
    "description": "Project description",
    "start_date": "2024-01-01",
    "end_date": "2024-12-31"
  }
  ```
- **Responses:**
  - `201 Created`: Returns created project
  - `400 Bad Request`: Validation errors

#### Retrieve Project
- **URL:** `/projects/{pk}/`
- **Method:** `GET`
- **Responses:**
  - `200 OK`: Returns project details
  - `404 Not Found`: Project does not exist

#### Update Project
- **URL:** `/projects/{pk}/`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "name": "Updated Project",
    "description": "Updated description",
    "start_date": "2024-01-01",
    "end_date": "2024-12-31"
  }
  ```
- **Responses:**
  - `200 OK`: Returns updated project
  - `400 Bad Request`: Validation errors
  - `404 Not Found`: Project does not exist

#### Delete Project
- **URL:** `/projects/{pk}/`
- **Method:** `DELETE`
- **Responses:**
  - `204 No Content`: Successfully deleted
  - `404 Not Found`: Project does not exist

### Tasks

#### List Tasks
- **URL:** `/projects/{project_id}/tasks/`
- **Method:** `GET`
- **Description:** Retrieve tasks for a specific project
- **Response:** `200 OK`

#### Create Task
- **URL:** `/projects/{project_id}/tasks/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "title": "New Task",
    "description": "Task description",
    "due_date": "2024-01-15"
  }
  ```
- **Responses:**
  - `201 Created`: Returns created task
  - `400 Bad Request`: Validation errors

#### Retrieve Task
- **URL:** `/tasks/{pk}/`
- **Method:** `GET`
- **Responses:**
  - `200 OK`: Returns task details
  - `404 Not Found`: Task does not exist

#### Update Task
- **URL:** `/tasks/{pk}/`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "title": "Updated Task",
    "description": "Updated description",
    "due_date": "2024-01-20"
  }
  ```
- **Responses:**
  - `200 OK`: Returns updated task
  - `400 Bad Request`: Validation errors
  - `404 Not Found`: Task does not exist

#### Delete Task
- **URL:** `/tasks/{pk}/`
- **Method:** `DELETE`
- **Responses:**
  - `204 No Content`: Successfully deleted
  - `404 Not Found`: Task does not exist

### Comments

#### List Comments
- **URL:** `/tasks/{task_id}/comments/`
- **Method:** `GET`
- **Description:** Retrieve comments for a specific task
- **Response:** `200 OK`

#### Create Comment
- **URL:** `/tasks/{task_id}/comments/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "content": "This is a comment."
  }
  ```
- **Responses:**
  - `201 Created`: Returns created comment
  - `400 Bad Request`: Validation errors

#### Retrieve Comment
- **URL:** `/comments/{pk}/`
- **Method:** `GET`
- **Responses:**
  - `200 OK`: Returns comment details
  - `404 Not Found`: Comment does not exist

#### Update Comment
- **URL:** `/comments/{pk}/`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "content": "Updated comment content."
  }
  ```
- **Responses:**
  - `200 OK`: Returns updated comment
  - `400 Bad Request`: Validation errors
  - `404 Not Found`: Comment does not exist

#### Delete Comment
- **URL:** `/comments/{pk}/`
- **Method:** `DELETE`
- **Responses:**
  - `204 No Content`: Successfully deleted
  - `404 Not Found`: Comment does not exist

## Setup Instructions
1. Replace `http://127.0.0.1:8000` with your actual domain
2. Ensure your models and serializers match the documented request/response fields
3. Add any additional project-specific setup requirements
