import json
import requests
import allure
from allure_commons.types import AttachmentType
from selene import browser, be
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

    def to_cart(self, url, **kwargs):
        add_to_cart_url = DOMAIN_URL + url
        cookie = self.response.cookies.get("NOPCOMMERCE.AUTH")
        requests.post(add_to_cart_url,
                      cookies={"NOPCOMMERCE.AUTH": cookie},
                      **kwargs)

    def api_log(self, url, **kwargs):
        result = requests.post(f'{DOMAIN_URL}{url}', **kwargs)

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

    def should_item_in_cart(self):
        browser.element('.ico-cart .cart-label').click()
        browser.element(".qty [value = '1']").should(be.visible)

    def delete_from_cart(self):
        browser.element('#topcartlink').click()
        browser.element('td.remove-from-cart input[type=checkbox]').should(
            be.visible).click()
        browser.element('.update-cart-button').click()


add_item = AddingItemsToCart()
