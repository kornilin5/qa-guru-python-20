from selene import browser, have
from tests.conftest import DOMAIN_URL, LOGIN, PASSWORD
import requests
from time import sleep


class AuthorizationPages:

    def open(self):
        browser.open(DOMAIN_URL)

    def log_in(self):
        self.open()
        response = requests.post(url=DOMAIN_URL + "login",
                                 data={
                                     "Email": LOGIN,
                                     "Password": PASSWORD
                                 },
                                 allow_redirects=False)
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        browser.driver.add_cookie({
            "name": "NOPCOMMERCE.AUTH",
            "value": cookie
        })

    def should_be_successful(self):
        browser.element('.account').should(have.text(LOGIN))


authorization_pages = AuthorizationPages()
