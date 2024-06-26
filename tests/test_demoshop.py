from allure_commons._allure import step
from qa_guru_python_20.models.page.adding_items_to_cart import add_item
from qa_guru_python_20.models.page.authorization_pages import authorization_pages


def test_login_api():
    """Successful authorization to some demowebshop (UI)"""
    with step("Fill login form"):
        authorization_pages.log_in()
    with step("Open login page"):
        authorization_pages.open()
    with step("Verify successful authorization"):
        authorization_pages.should_be_successful()


def test_add_to_cart_api():
    """Successful add item to cart (API)"""
    with step("Open login page"):
        add_item.open()
    with step("Fill login form"):
        add_item.log_in()
    with step("Add item to cart"):
        add_item.to_cart('addproducttocart/catalog/31/1/1')
    with step('Should item in cart'):
        add_item.should_item_in_cart()
    with step("logging response"):
        data_product = {"addtocart_31.EnteredQuantity": 1}
        add_item.api_log('addproducttocart/catalog/31/1/1', data=data_product)
    with step('delete item from cart'):
        add_item.delete_from_cart()


def test_add_phones_to_cart_api():

    with step("Open login page"):
        add_item.open()
    with step("Fill login form"):
        add_item.log_in()
    with step("Add item to cart"):
        add_item.to_cart('addproducttocart/catalog/43/1/1')
    with step('Should item in cart'):
        add_item.should_item_in_cart()
    with step("logging response"):
        data_product = {'addtocart_43.EnteredQuantity': 1}
        add_item.api_log('addproducttocart/catalog/43/1/1', data=data_product)
    with step("Delete item from cart"):
        add_item.delete_from_cart()
