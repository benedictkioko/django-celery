## Celery

Celery app will be created in the project root to collect all tasks defined across all Django apps listed in the INSTALLED_APPS configuration.

Let`s create celery task that generates a number of random User accounts.

We start by installing celery

`$ pip install celery`

starting worker

`celery -A managetasks worker -l info`