import os
from dotenv import load_dotenv

DOMAIN_URL = 'https://demowebshop.tricentis.com/'
LOGIN = os.getenv('LOGIN_USER')
PASSWORD = os.getenv('PASSWORD_USER')

load_dotenv()
