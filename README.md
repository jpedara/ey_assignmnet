# User Activity API
This is a Django-based API that provides endpoints for accessing user and activity period data.

## Installation:

1.  Clone this repository to your local machine.
2.  Create a virtual environment and activate it.
3.  Install the required packages by running 
    -   `pip install -r requirements.txt`.
4.  Create a SQLite database by running below commands
    -   `python manage.py makemigrations users`
    -   `python manage.py migrate`  
5.  Populate the database with dummy data by running 
    -   `python manage.py populate_db 10 3` 
    -    it will create 3 activites for 10 users
6.  Start the development server using 
    -   `python manage.py runserver`

## Authentication
This API does not require authentication to access.

## Folder Structure
```
project/
│
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
|   ├── management
|   |   └── commands
|   |          └── populate_db.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── user_activity/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## Models

### User

The User model represents a user of the application. It has the following fields:

-   `id`: A unique identifier for the user (auto-generated).
-   `real_name`: The user's real name.
-   `tz`: The user's timezone.

### ActivityPeriod

The ActivityPeriod model represents a period of activity for a user. It has the following fields:

-   `id`: A unique identifier for the activity period (auto-generated).
-   `user`: A foreign key to the user associated with the activity period.
-   `start_time`: The start time of the activity period.
-   `end_time`: The end time of the activity period.




## Serializers

The application has two serializers:

### UserSerializer

    This serializer is used to serialize a `User` instance.   
    It serializes the `id`, `real_name`, and `tz` fields.

### ActivityPeriodSerializer

    This serializer is used to serialize an `ActivityPeriod` instance.   
    It serializes the `id`, `start_time`, `end_time`, and `user` fields.     
    The `user` field is serialized using the `UserSerializer`.                 
    

## URLs
The application has two URLs:

### /users
This returns a list of all users along with activity periods in the system.

### /users/:id
This URL returns a specific user and corresponding activity period in the system.


# Deployement

This application has been deployed to a production environment using a cloud hosting platform PythonAnywhere.       

Below are the links to access the users:
```
    -   https://jpedara.pythonanywhere.com/users/
    -   https://jpedara.pythonanywhere.com/users/W012ABC1
```
