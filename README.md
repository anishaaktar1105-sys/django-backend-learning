# django-backend-learning

Learning Python backend development, Django, APIs, databases, and deployment through hands-on practice.

## Learning Progress

### Day 1 — Django Setup & First App

**What I Learned:**
- Created a Python virtual environment.
- Installed Django.
- Created a Django project using `django-admin startproject`.
- Explored the project structure.
- Ran the Django development server.
- Applied database migrations.
- Created and registered the `core` app.

**Files Created/Modified:**
- `manage.py`
- `config/settings.py`
- `config/urls.py`
- `config/asgi.py`
- `config/wsgi.py`
- `core/`

### Day 2 — Django Views and URL Routing

**What I Learned:**
- Created function-based views.
- Handled HTTP requests using `HttpResponse`.
- Created Home and About pages.
- Configured app-level URL patterns.
- Connected app URLs to project URLs using `include()`.
- Returned dynamic content from views.

**Files Created/Modified:**
- `core/views.py`
- `core/urls.py`
- `config/urls.py`

### Day 3 — Multiple Apps and URL Routing

**What I Learned:**
- Created two Django apps: `blog` and `shop`.
- Registered both apps in `INSTALLED_APPS`.
- Created views using `HttpResponse`.
- Configured separate URL patterns for each app.
- Connected both apps to the main project using `include()`.
- Created Blog Home, Blog About, Shop Home, and Products pages.
- Tested the routes in the browser.

**Files Created/Modified:**
- `config/settings.py`
- `config/urls.py`
- `blog/views.py`
- `blog/urls.py`
- `shop/views.py`
- `shop/urls.py`

### Day 4 — Django URL Parameters: `path()`, `re_path()` & `kwargs`

**What I Learned:**
- Learned dynamic URL parameters.
- Used `path()` to capture URL values.
- Passed parameters from URLs to views.
- Worked with `year`, `month`, and `day` parameters.
- Used `re_path()` for regular-expression-based URL routing.
- Implemented dynamic blog URLs.

**URL Examples:**
- `/blog/post/1/` — Post details
- `/blog/user/anisha/` — User profile
- `/blog/article/2024/04/30/` — Article by date
- `/blog/article/2024/` — Article by year

**Files Created/Modified:**
- `README.md`
- `myProject2/blog/`
- `myProject2/blog/urls.py`
- `myProject2/myProject2/urls.py`
- `myProject2/myProject2/settings.py`

### Day 5 — Django Templates: Project-Level Setup & HTML Rendering

**What I Learned:**
- Learned about Django's template system.
- Created a project-level `templates` folder.
- Created and rendered `home.html`.
- Configured the `TEMPLATES` setting in `settings.py`.
- Used `render()` to return an HTML page.
- Connected views and URLs to display templates.

**Practical Implementation:**
Created a webpage displaying the title *My First Webpage*, the heading *Hello World*, and a paragraph.

**Files Created/Modified:**
- `myProject3/templates/home.html`
- `myProject3/myProject3/views.py`
- `myProject3/myProject3/urls.py`
- `myProject3/myProject3/settings.py`

### Day 6 — Django Template Inheritance & Reusable Templates

**What I Learned:**
- Worked with shared templates and reusable layouts.
- Practised template inheritance.
- Organised templates for the `blog` and `shop` apps.
- Worked with template blocks and extending base templates.
- Updated template paths and URL configurations.
- Reduced code duplication by sharing layouts.

**Files Created/Modified:**
- `myProject4/blog/templates/blog/post_list.html`
- `myProject4/shop/templates/shop/product_list.html`
- `myProject4/myProject4/urls.py`
- `myProject4/myProject4/templates/base.html` (removed during restructuring)