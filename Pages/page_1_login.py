import allure
from Base.Base_Page import BasePage
from Configs.Links import Links

class LoginPage(BasePage):

    PAGE_URL = Links.host

    LOGIN_FIELD = 'data-test=username'
    PASSWORD_FIELD = 'data-test=password'
    LOGIN_BUTTON = 'data-test=login-button'
    ERROR_BOX = 'data-test=error'

    @allure.step('Enter login')
    async def enter_login(self, login):
        login_field = self.page.locator(self.LOGIN_FIELD)
        await self.expect(login_field).to_be_visible()
        await login_field.fill(login)

    @allure.step('Enter password')
    async def enter_password(self, password):
        password_field = self.page.locator(self.PASSWORD_FIELD)
        await self.expect(password_field).to_be_visible()
        await password_field.fill(password)

    @allure.step('Click submit button')
    async def click_submit(self):
        submit =  self.page.locator(self.LOGIN_BUTTON)
        await self.expect(submit).to_be_enabled()
        await submit.click()


    @allure.step('Check the error text')
    async def get_error_message_text(self):
        try:
            error = self.page.locator(self.ERROR_BOX)
            await self.expect(error).to_be_visible()
            return error.inner_text
        except:
            return None