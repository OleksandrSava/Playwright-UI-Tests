import allure
import pytest
from Base.Base_Test import BaseTest

@allure.feature('E2E test for purchase')
class TestFullPurchase(BaseTest):

    @allure.title("Purchase")
    @allure.severity("Blocker")
    @pytest.mark.asyncio
    async def test_purchase(self, prepare_checkout):
        info = ('Name', 'LastName', '30-500')

        await self.checkout_step_1_page.fill_checkout_form(*info)
        await self.checkout_step_1_page.click_continue()

        await self.checkout_step_2_page.open_check()
        await self.checkout_step_2_page.click_finish_button()

        await self.checkout_step_complete_page.open_check()
        await self.checkout_step_complete_page.click_back_button()

        await self.products_page.open_check()