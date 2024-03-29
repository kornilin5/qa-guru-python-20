from selene import browser
from tests.conftest import DOMAIN_URL, LOGIN, PASSWORD
import requests


class AddingItemsToCart:

    def __init__(self):
        self.response = requests.post(url=DOMAIN_URL + "login",
                                      data={
                                          "Email": LOGIN,
                                          "Password": PASSWORD
                                      },
                                      allow_redirects=False)

    def open(self):
        browser.open(DOMAIN_URL + "login")

    def log_in(self):
        cookie = self.response.cookies.get("NOPCOMMERCE.AUTH")
        self.open()
        browser.driver.add_cookie({
            "name": "NOPCOMMERCE.AUTH",
            "value": cookie
        })

    def to_cart(self):

        add_to_cart_url = DOMAIN_URL + "addproducttocart/catalog/31/1/1"
        cookie = self.response.cookies.get("NOPCOMMERCE.AUTH")
        requests.post(add_to_cart_url, cookies={"NOPCOMMERCE.AUTH": cookie})


add_item = AddingItemsToCart()
