import allure
import pytest
from Base.Base_Test import BaseTest

@allure.feature('Sort functionality')
class TestProducts(BaseTest):

    @allure.title("Purchase")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.asyncio
    async def test_sort(self, prepare_login):

        await self.products_page.open_check()

        sorted_az_names = await self.products_page.return_all_product_names()

        await self.products_page.select_option_za()
        expected_to_be_sorted_za = await self.products_page.return_all_product_names()

        assert expected_to_be_sorted_za == sorted(sorted_az_names, reverse=True), "ZA sort doesn't work"

        await self.products_page.select_option_hilo()
        all_prices_high_to_low = await self.products_page.return_all_product_prices()

        for i in range(len(all_prices_high_to_low) - 1):
            assert all_prices_high_to_low[i] >= all_prices_high_to_low[i+1], "High to low sort doesn't work"