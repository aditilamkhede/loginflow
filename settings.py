# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

# # OR, the same with increased verbosity
# load_dotenv(verbose=True)
#
# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SERVER_HOST = os.getenv("SERVER_HOST")
FROM_EMAIL=os.getenv("FROM_EMAIL")
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
# SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
