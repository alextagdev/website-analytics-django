# Web Statistics Application

This is a web statistics application built with Django, designed to retrieve and display information about a given website. The application checks the website's IP address, title, description, and image content to ensure they are in English.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Django: `pip install django`
- Django Compressor: `pip install django-compressor`
- Django Tailwind: `pip install django-tailwind`
- Requests: `pip install requests`
- Beautiful Soup 4: `pip install beautifulsoup4`

### Installation

###. Clone the repository:

   ```bash
   git clone https://github.com/alextag/web_statistics.git
Navigate to the project directory:

bash
Copy code
cd web_statistics
### Install the required dependencies:
pip install django
pip install django-compressor
pip install django-tailwind
pip install requests
pip install beautifulsoup4

### Start
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/web/ to access the web statistics application.

Features
Check IP address, title, description, and image content of a website.
