# django-backend-learning
learning Python backend development, Django, APIs, databases, and deployment through hands-on practice.


## Learning Progress

### Day 1 — Git & GitHub Basics
- Installed Git on Windows.
- Configured Git username and email.
- Created a GitHub repository.
- Learned how to clone a repository.
- Practised staging, committing, and pushing changes.

### Day 2 — Django Setup & First App
- Created a Python virtual environment.
- Installed Django.
- Created a Django project using `django-admin startproject`.
- Explored the project structure, including `manage.py` and the `config` folder.
- Ran the Django development server locally.
- Applied database migrations.
- Created my first Django app: `core`.
- Registered `core` in `INSTALLED_APPS` in `config/settings.py`.
- Used Git to track and upload my progress to GitHub.

## Tech Stack

- Python
- Django
- SQLite
- Git and GitHub

## Day-3
- Introduction to Django Views and URLs
- Creating function-based views
- Handling HTTP requests using HttpResponse
- Creating Home and About pages
- Configuring app-level URL patterns using core/urls.py
- Connecting app URLs to project URLs using include()
- Returning dynamic content from views using Python variables
- Testing URL endpoints locally


## Day-4:Creating Multiple Apps with Views and URL Routing
Today's Goal: Learn how to create multiple Django apps within a single project and configure their URL patterns.

What I Learned:
- Created two Django apps: blog and shop.
- Registered the apps in INSTALLED_APPS in settings.py.
- Created views using HttpResponse.
- Configured separate urls.py files for each app.
- Connected both apps to the main project using include().
- Created a home page and an about page for the Blog app.
- Created a home page and a products page for the Shop app.
- Ran the development server and tested the routes in the browser.

