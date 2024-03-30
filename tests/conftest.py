import os
from dotenv import load_dotenv
import pytest
from selene import browser

load_dotenv()
DOMAIN_URL = 'https://demowebshop.tricentis.com/'
LOGIN = os.getenv('LOGIN_USER')
PASSWORD = os.getenv('PASSWORD_USER')


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser.config.base_url = "DOMAIN_URL"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser

    browser.quit()
