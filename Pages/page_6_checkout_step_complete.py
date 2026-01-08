import allure
from Base.Base_Page import BasePage
from Configs.Links import Links

class CheckoutCompletePage(BasePage):

    PAGE_URL = Links.checkout_complete

    BACK_BUTTON = "data-test=back-to-products"

    @allure.step('Click back button')
    async def click_back_button(self):
        back = self.page.locator(self.BACK_BUTTON)
        await self.expect(back).to_be_enabled()
        await back.click()

