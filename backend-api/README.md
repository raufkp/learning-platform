# The learning Platform

This is an Academical learning platform for Devops

## Run the code

`python app.py`

# Flask Learning Hub API

A beginner-friendly REST API project built with **Python and Flask** to learn backend development concepts such as routing, HTTP methods, JSON request handling, UUID generation, API endpoints, and Swagger API documentation.

The project uses an in-memory Python dictionary as a temporary database. It is designed primarily as a **learning project** to understand how a backend application receives requests, processes data, and returns JSON responses.

---

## 📌 Project Overview

This project implements a simple Flask-based backend for a learning hub.

It provides APIs for:

- Creating database tables
- Creating users
- Finding users
- Viewing all stored data
- Creating testimonials
- Creating courses
- Creating membership plans
- Creating Q&A entries
- Viewing API documentation using Swagger

The application currently stores data in a Python dictionary instead of a permanent database such as MySQL, PostgreSQL, or MongoDB.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Flask | Web framework |
| Flasgger | Swagger/OpenAPI documentation |
| UUID | Generating unique IDs |
| Datetime | Generating timestamps |
| JSON | Request and response data format |

---

## 📂 Project Structure

```text
flask-learning-hub/
│
├── app.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Prerequisites

Before running this project, make sure you have:

- Python 3.x
- pip
- Git
- A code editor such as VS Code
- Postman or another API testing tool

Check your Python installation:

```bash
python --version
```

Check pip:

```bash
pip --version
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd flask-learning-hub
```

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install flask flasgger
```

Alternatively, if `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

---

## 📄 requirements.txt

The project can use the following dependencies:

```text
Flask
flasgger
```

You can generate the file automatically with:

```bash
pip freeze > requirements.txt
```

---

# 🚀 Running the Application

Run the Flask application:

```bash
python app.py
```

The application will normally start at:

```text
http://127.0.0.1:5000
```

You should see output similar to:

```text
* Running on http://127.0.0.1:5000
* Debug mode: on
```

---

# 🌐 API Endpoints

## 1. Home Page

### Endpoint

```http
GET /
```

### Description

Returns a welcome message.

### Example

```bash
curl http://127.0.0.1:5000/
```

### Response

```text
Welcome to my learning hub!
```

---

# 2. Create a Table

### Endpoint

```http
POST /v1/ct
```

### Description

Creates a new table inside the in-memory `database` dictionary.

### Request Body

```json
{
    "table_name": "users"
}
```

### Example using curl

```bash
curl -X POST http://127.0.0.1:5000/v1/ct \
-H "Content-Type: application/json" \
-d "{\"table_name\":\"users\"}"
```

### Example Response

```json
{
    "message": "Database created successfully!",
    "status": 205,
    "database": {
        "users": {}
    }
}
```

---

# 3. Create User

### Endpoint

```http
POST /v1/uc
```

### Description

Creates a new user inside an existing table.

A unique user ID is automatically generated using Python's `uuid4()` function.

### Request Body

```json
{
    "table_name": "users",
    "user_name": "John",
    "email_id": "john@example.com"
}
```

### Example Response

```json
{
    "message": "User '<generated-user-id>' created successfully in table 'users'!",
    "status": 201,
    "database": {
        "users": {
            "<generated-user-id>": {
                "user_name": "John",
                "email_id": "john@example.com"
            }
        }
    }
}
```

---

# 4. Find User

### Endpoint

```http
GET /v1/fu/<table_name>/<uid>
```

### Description

Retrieves a user from a specified table using the user's unique ID.

### Example

```bash
curl http://127.0.0.1:5000/v1/fu/users/<USER_ID>
```

### Example Response

```json
{
    "table_name": "users",
    "user_id": "<USER_ID>",
    "user_data": {
        "user_name": "John",
        "email_id": "john@example.com"
    }
}
```

---

# 5. Get All Users / Database

### Endpoint

```http
GET /gt
```

### Description

Returns all data currently stored in the in-memory database.

### Example

```bash
curl http://127.0.0.1:5000/gt
```

### Response

```json
{
    "database": {
        "users": {
            "<USER_ID>": {
                "user_name": "John",
                "email_id": "john@example.com"
            }
        }
    }
}
```

---

# 6. Create Testimonial

### Endpoint

```http
POST /v1/testimonials
```

### Description

Creates a testimonial containing author information, content, rating, status, and a generated ID.

### Request Body

```json
{
    "author_name": "John Doe",
    "content": "This learning platform is very useful.",
    "rating": 5,
    "status": "published"
}
```

### Example Response

```json
{
    "message": "Testimonial created successfully!"
}
```

---

# 7. Create Course

### Endpoint

```http
POST /v1/courses
```

### Description

Creates a course with information such as title, description, category, level, and status.

### Request Body

```json
{
    "title": "Python for Beginners",
    "description": "Learn Python programming from the basics.",
    "category": "Programming",
    "level": "Beginner",
    "status": "active",
    "created_by": "admin"
}
```

### Example Response

```json
{
    "message": "Course created successfully!"
}
```

---

# 8. Create Membership Plan

### Endpoint

```http
POST /v1/membershipplans
```

### Description

Creates a membership plan.

### Request Body

```json
{
    "name": "Premium",
    "description": "Premium learning membership",
    "currency": "INR",
    "duration": "3 months",
    "features": [
        "Premium Courses",
        "Live Sessions",
        "Community Access"
    ],
    "status": "active"
}
```

### Example Response

```json
{
    "message": "Membership plan created successfully!"
}
```

---

# 9. Create Q&A

### Endpoint

```http
PUT /v1/qa
```

### Description

Creates a question-and-answer entry.

### Request Body

```json
{
    "question": "What is Flask?",
    "answer": "Flask is a lightweight Python web framework.",
    "asked_by": "Student",
    "answered_by": "Instructor",
    "status": "published"
}
```

### Example Response

```json
{
    "message": "Q&A created successfully!"
}
```

---

# 📚 Swagger API Documentation

The application uses **Flasgger** to provide Swagger documentation.

After starting the application, open:

```text
http://127.0.0.1:5000/apidocs/
```

Swagger provides an interactive interface where you can explore and test the API endpoints.

---

# 🧠 Python Concepts Demonstrated

This project is useful for practicing several important Python concepts.

### Dictionary

The project uses:

```python
database = {}
```

The dictionary acts as a temporary in-memory database.

---

### Functions

Each API endpoint is implemented using a Python function:

```python
def create_user():
```

---

### Decorators

Flask decorators are used to connect URLs to functions:

```python
@app.post("/v1/uc")
def create_user():
```

The decorator tells Flask which URL and HTTP method should trigger the function.

---

### UUID

The project uses:

```python
uuid4()
```

to generate unique identifiers.

Example:

```python
user_id = str(uuid4())
```

---

### JSON

Incoming JSON data is accessed using:

```python
data = request.get_json()
```

Values can then be retrieved using:

```python
user_name = data.get("user_name")
```

---

### HTTP Status Codes

The application returns HTTP status codes such as:

```text
200 OK
201 Created
400 Bad Request
404 Not Found
```

---

### Path Parameters

The user lookup endpoint demonstrates URL path parameters:

```python
@app.get("/v1/fu/<table_name>/<uid>")
```

Here:

```text
table_name
uid
```

are extracted from the URL and passed to the function.

---

# 🔄 Request Flow

A simplified request flow looks like this:

```text
Client
  |
  | HTTP Request
  v
Flask Application
  |
  | Route Matching
  v
View Function
  |
  | Process Request
  v
In-Memory Dictionary
  |
  | JSON Response
  v
Client
```

For example:

```text
Postman
   |
   | POST /v1/uc
   v
Flask Route
   |
   v
create_user()
   |
   v
Generate UUID
   |
   v
Store User
   |
   v
Return JSON Response
```

---

# 🧪 Testing with Postman

You can use Postman to test the APIs.

For example:

### Method

```text
POST
```

### URL

```text
http://127.0.0.1:5000/v1/uc
```

### Body

Select:

```text
Body → raw → JSON
```

Then enter:

```json
{
    "table_name": "users",
    "user_name": "Abdu",
    "email_id": "abdu@example.com"
}
```

Click **Send**.

---

# ⚠️ Current Project Limitations

This project is currently designed for learning and has several limitations.

### 1. In-memory database

The application uses:

```python
database = {}
```

Therefore, all data will be lost when the Flask application stops or restarts.

A real application should use a persistent database such as:

- PostgreSQL
- MySQL
- MongoDB
- SQLite

---

### 2. Limited input validation

The application currently does not validate all incoming fields.

For example, a course can potentially be created without checking whether every required field contains valid data.

---

### 3. Error handling can be improved

Some endpoints should handle cases such as:

- Missing JSON body
- Invalid JSON
- Non-existent tables
- Non-existent users
- Invalid data types
- Duplicate records

---

### 4. Debug mode

The application currently uses:

```python
app.run(debug=True)
```

Debug mode is useful during development but should **not be enabled in production**.

---

### 5. Some variables are currently unused

For example:

```python
created_at
updated_at
created_by
```

are assigned in some functions but are not currently stored in the database structure.

These can be incorporated in a future version.

---

# 🔧 Future Improvements

Possible improvements for this project include:

- Add PostgreSQL/MySQL database
- Add SQLAlchemy
- Add complete CRUD operations
- Add authentication and authorization
- Add JWT authentication
- Improve request validation
- Add centralized error handling
- Add database models
- Add unit tests
- Add integration tests
- Improve Swagger/OpenAPI documentation
- Add logging
- Add environment variables
- Add Docker support
- Deploy the API to AWS
- Add CI/CD using GitHub Actions

---

# 🎯 Learning Objectives

By completing this project, you can gain practical experience with:

- Python functions
- Flask application structure
- Flask routing
- HTTP methods
- REST API concepts
- GET requests
- POST requests
- PUT requests
- Path parameters
- JSON request bodies
- JSON responses
- HTTP status codes
- UUID generation
- Swagger/OpenAPI
- API testing with Postman
- Git and GitHub

---

# 🔗 Useful API Summary

| Method | Endpoint | Purpose |
|---|---|---|
| GET/POST | `/` | Home page |
| POST | `/v1/ct` | Create table |
| POST | `/v1/uc` | Create user |
| GET | `/v1/fu/<table_name>/<uid>` | Find user |
| GET | `/gt` | Get all database data |
| POST | `/v1/testimonials` | Create testimonial |
| POST | `/v1/courses` | Create course |
| POST | `/v1/membershipplans` | Create membership plan |
| PUT | `/v1/qa` | Create Q&A |
| GET | `/apidocs/` | Swagger documentation |

---

# 👨‍💻 Author

**Abdu Raoof**

Python & Backend Development Learning Project

---

# 📜 License

This project is created for educational and learning purposes.
