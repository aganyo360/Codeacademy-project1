# Vidly - Django Movie App

## Overview

Vidly is a Django application that displays movies along with their genres, ratings, year of release, title, and stock availability. The app uses Bootstrap for styling and HTML for the front end. It also includes an API for accessing movie data.

## Features

- Display a list of movies with details:
  - Title
  - Genre
  - Rating
  - Year of Release
  - Number of Stock Available
- API for accessing movie data
- Responsive design using Bootstrap

## Technologies Used

- Django
- Bootstrap
- HTML
- SQLite (default database)
- Javascript

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/aganyo360/Django_API.git
   cd Django_API


2. Create a virtual environment and activate it
     ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install the required dependencies:
    ```sh
        pip install -r requirements.txt
 
4. Apply migrations:
    ```sh
        python manage.py migrate
5. Run the development server:
    ```sh
        python manage.py runserver
6. Access the application: <br>
    Open your web browser and navigate to http://127.0.0.1:8000.


## Usage
#### Add Movies:

Navigate to the admin panel at http://127.0.0.1:8000/admin and log in with your admin credentials. <br>
Add movie entries including title, genre, rating, year of release, and stock availability.
View Movies:

Visit the home page to see the list of available movies along with their details.
API Access:

Access the API endpoints at http://127.0.0.1:8000/api/movies to retrieve movie data.

# Project structure
 Django_API/ <br>
├── api/<br>
│   ├── migrations/<br>
│   ├── __init__.py<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── serializers.py<br>
│   ├── tests.py<br>
│   ├── urls.py<br>
│   ├── views.py<br>
├── movies/<br>
│   ├── migrations/<br>
│   ├── static/<br>
│   ├── templates/<br>
│   ├── __init__.py<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── tests.py<br>
│   ├── urls.py<br>
│   ├── views.py<br>
├── vidly/<br>
│   ├── __init__.py<br>
│   ├── asgi.py<br>
│   ├── settings.py<br>
│   ├── urls.py<br>
│   ├── wsgi.py<br>
├── db.sqlite3<br>
├── manage.py<br>
├── requirements.txt<br>

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Live Demo
Check out the live demo of the project at https://vidly.shahibu.com.

#### Contact
If you have any questions or suggestions, feel free to contact me at wilsonaganyo@gmail.com.

