# Social-Media-Application-BRD

## Project Description
This project is a simple social media web application built with Django for the backend and HTML, CSS, and JavaScript for the frontend. It mimics a basic version of Facebook, allowing users to register, log in, create posts and view posts on a global feed or on their personal profile page. Users can also edit or delete their own posts. The app features a clean, intuitive interface with a navigation bar and footer for easy site navigation.

## Setup Instructions

Follow these steps to set up and run the application locally:

1. Download these files and run locally
2. Create and activate Virtual environment
   python -m venv env
   source env/bin/activate
3. Install Django
   pip install django
4. Apply database migrations
   python manage.py makemigrations
   python manage.py migration
5. create superuser
   python manage.py createsuperuser
6. Run server
   python manage.py runserver 3000

   
Sample User Credentials for Testing
  Role	      Username	    Password
  Superuser	  admin	        admin
  Regular     user 1	      user1	
  Regular     user 2	      user2


Implemented Features Summary

1. User registration with username, email, password, and password confirmation
2. User authentication with login and logout
3. Global homepage displaying all users' posts (text and optional images)
4. Profile page showing only the logged-in user's posts, with options to edit or delete
5. Post creation, editing, and deletion restricted to post owners only
6. Navbar with links to homepage, profile, login/logout, and registration
7. Footer with basic site information
8. User feedback via Django messages (e.g., success notifications)
9. Secure access control using Django authentication mixins and decorators


ER Diagram

