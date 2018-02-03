AURN-API V2
------------

REST API for UK air quality data collected from live measurements published by a government agency.
Built using the Django-Rest-Framework along with the Swagger API documentation tool.

The API for an updated collection of air quality data is available online from the root URL:  http://ukair.pauljd.me. The Django application was deployed using Amazon Web Services and it uses an AWS Lambda function triggered on an hourly basis by CloudWatch Events.

URL Routes
----------
Api Root: http://127.0.0.1:8000/

**docs/**

auto-generated documentation detailing endpoints which serve GET requests

**current-data/**
data for each monitoring site for the most recent hour

**sites/**

site information for all monitoring sites

**sites/<site_id>**

site information for a specified monitoring site

**data/**

data for each monitoring site for the current date

**data/<date_1>**

data for each monitoring site for a specified date in format YYYY-MM-DD

**data/<date_1>/<date_2>**

data for each monitoring site between a range of dates with format YYYY-MM-DD

**site-data/<site_code>/<number_of_days>/**

data for a specified monitoring site from a specified number of recent days

e.g. site-data/MY1/5/ retrieves London Marylebone Road data from the past 5 days




Getting Started
---------------


**Prerequisites**

Python 3.4, pip, virtualenv

**1. Clone or copy repository**

**2. Set up Virtual Environment**

Create a virtual environment named aurn-venv:

    $ virtualenv aurn-venv

Activate the virtual environment:

    $ source aurn-venv/bin/activate
    (aurn-venv) $

Use *pip* to install requirements:

    (aurn-venv) $ pip install requirements.txt

Verify that packages have been installed:

    (aurn-venv) $ pip freeze
    Django==2.0
    pytz==2017.3
    python-dateutil==2.6.1
    requests==2.13.0
    beautifulsoup4==4.6.0
    djangorestframework==3.7.7
    django-rest-swagger==2.1.2
    lxml==4.1.1
    psycopg2==2.7.3.2

**3. Run migrations and management commands**

Specify database settings, run initial migrations and then enter the following management commands within the project root directory to populate the Site table and obtain recent hourly data:

    $ python manage.py addsites

    $ python manage.py collectdata
    
    
Current air quality data is updated every hour on a government agency webpage. A database can be populated by scraping the relevant values and saving them to a database on an hourly basis.
To carry out this process, run the management command from the project root directory: python manage.py collectdata

**4. Run the server**

    $ python manage.py runserver
