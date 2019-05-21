##Celery

Celery app we created in the project root will collect all tasks defined across all Django apps listed in the INSTALLED_APPS configuration.

Let`s create celery task that generates a number of random User accounts.

lets start by installing celery

`$ pip install celery`

starting worker

`celery -A managetasks worker -l info`