from celery import Celery
from celery.schedules import crontab
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from .tasks import file_opertion_task

celery = Celery(__name__)
celery.conf.broker_url = CELERY_BROKER_URL
celery.conf.result_backend = CELERY_RESULT_BACKEND


celery.conf.beat_schedule = {
    "create_task": {
        "task": "create_file",
        "schedule": 89.0,
    },
}
celery.conf.timezone = "UTC"


@celery.task(name = "create_file")
def create_file():
     file_opertion_task()
