import allure
import re
from Base.Base_Page import BasePage
from Configs.Links import Links


class ProductsPage(BasePage):

    PAGE_URL = Links.inventory

    class Locators:
        DROPDOWN = "data-test=product-sort-container"
        OPTION_ZA = '//div//select/option[@value="za"]'
        OPTION_HILO = '//div//select/option[@value="hilo"]'
        CART_BUTTON = "data-test=shopping-cart-link"
        PRODUCTS_NAME = "data-test=inventory-item-name"
        PRODUCTS_PRICE = "data-test=inventory_item_price"
        ADD_FIRST_BUTTON = '(//button[@class="btn btn_primary btn_small btn_inventory "])[1]'
        ADD_SECOND_BUTTON = '(//button[@class="btn btn_primary btn_small btn_inventory "])[2]'

    async def add_to_cart(self):
        two_first_products = [
            self.page.locator(self.Locators.ADD_FIRST_BUTTON),
            self.page.locator(self.Locators.ADD_SECOND_BUTTON)
        ]
        for idx, button in enumerate(two_first_products):
            with allure.step(f'Adding {idx} locator to cart'):
                await self.expect(button).to_be_enabled()
                await button.click()

    @allure.step('Select option ZA (Name Z to A)')
    async def select_option_za(self):
        select = self.page.locator('select[data-test="product-sort-container"]')
        await self.expect(select).to_be_enabled()
        await select.select_option(value='za')  # або label='Name (Z to A)'

    @allure.step('Select option HILO (Price high to low)')
    async def select_option_hilo(self):
        select = self.page.locator('select[data-test="product-sort-container"]')
        await self.expect(select).to_be_enabled()
        await select.select_option(value='hilo')

    @allure.step('Click cart')
    async def click_cart(self):
        cart_button = self.page.locator(self.Locators.CART_BUTTON)
        await self.expect(cart_button).to_be_enabled()
        await cart_button.click()

    @allure.step('Find all product names')
    async def return_all_product_names(self):
        locator = self.page.locator(self.Locators.PRODUCTS_NAME)
        all_names = await locator.all_text_contents()
        return all_names

    @allure.step('Find all product prices')
    async def return_all_product_prices(self):

        locator = self.page.locator(self.Locators.PRODUCTS_PRICE)
        texts = await locator.all_text_contents()  # -> list[str], напр. ["$15.99", "$9.50", ...]
        prices = [float(re.sub(r'[^\d.]', '', t).strip()) for t in texts]
        return prices