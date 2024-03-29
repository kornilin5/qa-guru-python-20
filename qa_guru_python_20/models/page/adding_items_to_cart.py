import json
import requests
import allure
from allure_commons.types import AttachmentType
from allure_commons._allure import step
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
        self.open()
        cookie = self.response.cookies.get("NOPCOMMERCE.AUTH")
        browser.driver.add_cookie({
            "name": "NOPCOMMERCE.AUTH",
            "value": cookie
        })

    def to_cart(self):

        add_to_cart_url = DOMAIN_URL + "addproducttocart/catalog/31/1/1"
        cookie = self.response.cookies.get("NOPCOMMERCE.AUTH")
        requests.post(add_to_cart_url, cookies={"NOPCOMMERCE.AUTH": cookie})

    def api_log(self, **kwargs):
        result = requests.post(f'{DOMAIN_URL}addproducttocart/catalog/31/1/1',
                               **kwargs)

        allure.attach(body=result.request.url,
                      name="Request url",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=json.dumps(result.request.body,
                                      indent=4,
                                      ensure_ascii=True),
                      name="Request body",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        allure.attach(body=json.dumps(result.json(),
                                      indent=4,
                                      ensure_ascii=True),
                      name="Response",
                      attachment_type=AttachmentType.JSON,
                      extension="json")

        return result


add_item = AddingItemsToCart()
