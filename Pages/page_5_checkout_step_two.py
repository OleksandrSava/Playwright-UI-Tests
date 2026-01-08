import allure
from Base.Base_Page import BasePage
from Configs.Links import Links

class CheckoutStepTwoPage(BasePage):

    PAGE_URL = Links.checkout_2nd

    FINISH_BUTTON = "data-test=finish"

    @allure.step('Click on finish button')
    async def click_finish_button(self):
        finish = self.page.locator(self.FINISH_BUTTON)
        await self.expect(finish).to_be_enabled()
        await finish.click()
