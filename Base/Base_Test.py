import pytest_asyncio
from Configs.Data import Data
from Pages.page_1_login import LoginPage
from Pages.page_2_products import ProductsPage
from Pages.page_3_cart import CardPage
from Pages.page_4_checkout_step_one import CheckoutStepOnePage
from Pages.page_5_checkout_step_two import CheckoutStepTwoPage
from Pages.page_6_checkout_step_complete import CheckoutCompletePage


class BaseTest:

    data : Data

    login_page: LoginPage
    products_page: ProductsPage
    cart_page: CardPage
    checkout_step_1_page: CheckoutStepOnePage
    checkout_step_2_page: CheckoutStepTwoPage
    checkout_step_complete_page: CheckoutCompletePage

    @pytest_asyncio.fixture(autouse=True)
    async def setup(self, request, page):
        request.cls.page = page
        request.cls.data = Data()

        request.cls.login_page = LoginPage(page)
        request.cls.products_page = ProductsPage(page)
        request.cls.cart_page = CardPage(page)
        request.cls.checkout_step_1_page = CheckoutStepOnePage(page)
        request.cls.checkout_step_2_page = CheckoutStepTwoPage(page)
        request.cls.checkout_step_complete_page = CheckoutCompletePage(page)