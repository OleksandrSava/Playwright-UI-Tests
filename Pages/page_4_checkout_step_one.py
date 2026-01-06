import allure
from Base.Base_Page import BasePage
from Configs.Links import Links

class CheckoutStepOnePage(BasePage):

    PAGE_URL = Links.checkout_1th

    class Locators:
        FIRST_INPUT_FIELD = "data-test=firstName"
        SECOND_INPUT_FIELD = "data-test=lastName"
        POST_INPUT_FIELD = "data-test=postalCode"
        ERROR_BOX = "data-test=error"
        CONTINUE_BUTTON = "data-test=continue"

    @allure.step('Fill the form')
    async def fill_checkout_form(self, first_name, last_name, postal_code):
        fields = [
            (self.page.locator(self.Locators.FIRST_INPUT_FIELD), first_name),
            (self.page.locator(self.Locators.SECOND_INPUT_FIELD), last_name),
            (self.page.locator(self.Locators.POST_INPUT_FIELD), postal_code)
        ]
        for locator, value in fields:
            await self.expect(locator).to_be_visible()
            await locator.fill(value)

    @allure.step('Check error box text')
    async def get_error_box_text(self):
        try:
            error = self.page.locator(self.Locators.ERROR_BOX)
            await self.expect(error).to_be_visible()
            return error.inner_text
        except:
            return None

    @allure.step('Click continue button')
    async def click_continue(self):
        continue_button= self.page.locator(self.Locators.CONTINUE_BUTTON)
        await self.expect(continue_button).to_be_enabled()
        await continue_button.click()