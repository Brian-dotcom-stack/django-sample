# Django Cuisine App

A Django Web App for listing, viewing, and managing cuisine items with pagination, class-based views, and admin intergration.

## Features 

- List view of all cuisines with pagination
- Detail view for each cuisine item
- Class-based ListView and DetailView
- Template inheritancce with base.html
- Author display and publish date
- Image uploads for cuisine items
- Django admin intergration

## Installation

1. Clone the repository

``git clone <your-repo-url>``

2. Create and activate a virtual environment:

``python -m venv venv``

 ``venv\Scripts\activate``

3. Install dependencies:

``pip install -r requirements.txt``

4. Run migrations:

``python manage.py migrate``

5. Start the server:

``python manage.py runserver``

## Usage

Visit http://127.0.0.1:8000/cuisine/ to view the cuisine list.

Visit http://127.0.0.1:8000/admin/ to manage items in the Django admin.

## Future improvements

- Add Create/Update/Delete views
- Add search and filtering
- Add user authentication for posting cuisines
- Improve UI with Angular