import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

config = {
    'db_url': os.environ.get('DATABASE_URL'),
    'db_username': os.environ.get('DATABASE_USER'),
    'db_password': os.environ.get('DATABASE_USER_PASSWORD'),
}

auth_config = {
    'secret_key': os.environ.get('AUTH_SECRET_KEY'),
    'algorithm': os.environ.get('AUTH_ALGORITHM'),
    'access_token_expires_minutes': int(os.environ.get('AUTH_TOKEN_EXPIRATION_MINUTES'))
}