# importing celery app everytime django starts
from .celery import app as celery_app

__all__ = ['celery_app']
