import os
from dotenv import load_dotenv
import pytest
from selene import browser

DOMAIN_URL = 'https://demowebshop.tricentis.com/'
LOGIN = os.getenv('LOGIN_USER')
PASSWORD = os.getenv('PASSWORD_USER')

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser.config.base_url = "DOMAIN_URL"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser

    browser.quit()
