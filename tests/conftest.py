import os
from selene import browser

DOMAIN_URL = 'https://demowebshop.tricentis.com/'
USER_URL = DOMAIN_URL + '/users'
LOGIN = os.getenv('LOGIN_USER')
PASSWORD = os.getenv('PASSWORD_USER')
