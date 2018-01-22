Version 2 of a REST API providing UK air quality data collected from live measurements published by DEFRA.
Built using the Django-Rest-Framework.

The DEFRA webapge https://uk-air.defra.gov.uk/latest/currentlevels provides
current measurements and is updated on an hourly basis. The Data.update() static method
defined in api/models.py scrapes the relevant values and saves them to the database.
To run this method and update data, run the management command from the project root directory: py manage.py collectdata

The API providing data since 21/01/2018 is available online from the root URL:  http://aurn-api.pauljd.me. The Django application was deployed using Amazon Web Services and it uses an AWS Lambda function triggered on an hourly basis by CloudWatch Events.

URL Routes
----------
Api Root: http://127.0.0.1:8000/

**sites/**

site information for all monitoring sites

**sites/<site_id>**

site information for a specified monitoring site

**site-data/<site_code>**

data for all time points for a specified monitoring site

e.g. site-data/MY1/ retrieves all data for London Marylebone Road

**site-data/<site_code>/<number_of_days>/**

data for a specified monitoring site from a specified number of recent days

e.g. site-data/MY1/5/ retrieves London Marylebone Road data from the past 5 days


**data/**

complete set of data (each time point for all monitoring sites)



