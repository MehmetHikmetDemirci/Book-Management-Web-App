# BookManagementSystem

BookManagementSystem is a Django-based book management system, facilitating the listing, adding, editing, and deletion of books.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9+
- pip (comes with Python)
- Virtualenv (optional but recommended)

### Installing

1. Clone the repository:

`https://github.com/MehmetHikmetDemirci/Book-Management-Web-App.git`

`cd BookManagementSystem`


2. Create and activate a virtual environment (optional):

`python -m venv venv`

`source venv/bin/activate` # For Unix or MacOS

`venv\Scripts\activate` # For Windows


3. Install the required packages:


`pip install -r requirements.txt`


4. Set up your database configurations in a `.env` file:


`DB_NAME=book_catalog`

`DB_USER=yourusername`

`DB_PASSWORD=your_secure_password`

`DB_HOST=localhost`


5. Run database migrations:


`python manage.py migrate`


6. Start the server:

`gunicorn BookManagementSystem.wsgi:application --bind localhost:$PORT`



Visit `http://localhost:$PORT` in your browser to access the application.

## Using Docker

To run the project with Docker:

1. Build the Docker image:


`docker build -t bookmanagementsystem .`


2. Run the Docker container:


`docker run -p 8000:8000 bookmanagementsystem`


## Running the Tests


To run the tests for the project:

`python manage.py test`


