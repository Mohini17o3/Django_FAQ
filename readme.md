Visit Deployed  : https://django-faqgunicorn-your-project-name.onrender.com/
# Django FAQ API Project

## Overview

This project is a Django-based FAQ management application that allows users to:

- View frequently asked questions (FAQs)
- Add new FAQs
- Manage and retrieve FAQ data via API
- Use HTML views for easy interaction with the system

The application provides both **web views** (for interacting with the FAQ system through a browser) and a **REST API** (for integrating the system with other services or for testing).

---

<img src='/public/1.png'>
<img src='/public/2.png'>
<img src='/public/3.png'>

## Features

- **CRUD operations** for FAQs
- **JSON API** for retrieving and posting FAQs
- **HTML views** for a user-friendly interface to add FAQs and view existing ones
- **Cache** for optimized API calls

---

## Setup and Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django 5.x (or latest stable)
- Redis (if caching is used, but optional for basic usage)
- Postman (for API testing)

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/your-repository-link.git
cd your-repository-folder
```

### 2. Set Up Virtual Environment

Create and activate a virtual environment to isolate the project dependencies.

On Windows:

```bash
python -m venv venv
./env/Scripts/activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Once the virtual environment is activated, install the necessary dependencies:

```bash
pip install -r requirements.txt

```

This will install all the required Python packages.

### 4. Set Up the Database

By default, Django uses SQLite as the database. If you want to use the default SQLite database, run:

```bash
python manage.py migrate

```

This will create the necessary database tables.

### 5. Start the Development Server

To run the application locally, start Django’s development server:

```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/.

### 6. Using the HTML Views

- Accessing the FAQ View:

  - Open your browser and go to http://127.0.0.1:8000/. This will load the page where you can view the list of FAQs.

- Adding New FAQ:
  - To add a new FAQ, go to the page where you can submit the FAQ details (http://127.0.0.1:8000/post_faq/).
  - Provide the FAQ question and language, and submit the form.

### Using Postman for API Testing

Apart from the html templates , you can test the API endpoints using Postman as well .

### 1. Get All FAQs (GET Request)

URL: http://127.0.0.1:8000/get_faqs/
Method: GET
Headers:
Accept: application/json
Response:
You will receive a JSON response containing all the FAQs.

### 2. Create a New FAQ (POST Request)

To create a new FAQ via API, use the following steps in Postman:

URL: http://127.0.0.1:8000/post_faqs/

Method: POST

Headers:
Content-Type: application/json Accept: application/json X-CSRFToken: {CSRF token from cookies}

### CSRF Token

For POST requests, Django requires a CSRF token for security purposes. You need to pass the CSRF token as part of the headers.

First, send a GET request to http://127.0.0.1:8000/ to load the page and get the CSRF token in the cookies.

In Postman, copy the CSRF token from the cookies section.

Add the CSRF token to the request header as X-CSRFToken.

Body (in JSON format) to be received :

```bash
{
  "question": "What is Django?",
  "language": "en"
}
```
