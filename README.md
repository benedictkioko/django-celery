## Celery

Celery app will be created in the project root to collect all tasks defined across all Django apps listed in the INSTALLED_APPS configuration.

##### Instructions
- Clone the repo `git clone git@github.com:benedictkioko/django-celery.git`

- Install celery and other required dependencies to run the project

`pip install -r requirements.txt`

Let`s create celery task that generates a number of random User accounts.

##### starting celery workers

`celery -A managetasks worker -l info`

##### Run the project

`python manage.py runserver 0.0.0.0:8000`