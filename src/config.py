from dotenv import load_dotenv
import os

load_dotenv()


DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")


DB_HOST_TEST = os.environ.get("DB_HOST")
DB_PORT_TEST = os.environ.get("DB_PORT")
DB_USER_TEST = os.environ.get("DB_USER")
DB_PASSWOR_TEST = os.environ.get("DB_PASSWORD")
DB_NAME_TEST = os.environ.get("DB_NAME")

CELERY_BROKER_URL =  os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")


