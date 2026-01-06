import allure
from Base.Base_Page import BasePage
from Configs.Links import Links


class CardPage(BasePage):

    PAGE_URL = Links.cart

    class Locators:
        REMOVE_BUTTON = f'(//div//button[@class="btn btn_secondary btn_small cart_button"])[2]'
        CHECKOUT_BUTTON = "data-test=checkout"

    @allure.step('Removing product from cart')
    async def remove_product(self):
        remove = self.page.locator(self.Locators.REMOVE_BUTTON)
        await self.expect(remove).to_be_enabled()
        await remove.click()

    @allure.step('Click checkout button')
    async def click_checkout(self):
        checkout = self.page.locator(self.Locators.CHECKOUT_BUTTON)
        await self.expect(checkout).to_be_enabled()
        await checkout.click()
