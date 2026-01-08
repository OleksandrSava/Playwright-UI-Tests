import allure
import pytest
from Configs.Data import Data
from Base.Base_Test import BaseTest


@allure.feature("Tests for login")
class TestLogin(BaseTest):

    @allure.severity("Blocker")
    @pytest.mark.smoke
    @pytest.mark.asyncio
    @pytest.mark.parametrize(

        'login, password, status',
    [
        (Data.LOGIN, 'Wrong password', False),
        ('Wrong login', Data.PASSWORD, False),
        ('', '', False),
        (Data.LOGIN, Data.PASSWORD, True),
    ],

        ids = [f"Login test {i + 1}" for i in range(4)]
    )
    async def test_login(self, login, password, status):
        await self.login_page.open()
        await self.login_page.open_check()

        await self.login_page.enter_login(login)
        await self.login_page.enter_password(password)
        await self.login_page.click_submit()

        if status:
            await self.products_page.open_check()
        else:
            error = await self.login_page.get_error_message_text()
            assert error is not None, "Expected error message, but none was displayed"
