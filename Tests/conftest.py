import pytest_asyncio
from Configs.Data import Data
from playwright.async_api import async_playwright

@pytest_asyncio.fixture(scope="function", autouse=True)
async def page(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=[
                "--headless=new",
                "--no-sandbox",
                "--disable-blink-features=AutomationControlled",
                "--start-maximized",
                "--disable-dev-shm-usage",
                "--disable-extensions",
                "--lang=en-US",          ]
        )

        page = await browser.new_page()
        request.cls.page = page
        yield page
        await browser.close()

@pytest_asyncio.fixture
async def prepare_login(request):

    prepare_login = request.cls

    await prepare_login.login_page.open()
    await prepare_login.login_page.open_check()
    await prepare_login.login_page.enter_login(Data.LOGIN)
    await prepare_login.login_page.enter_password(Data.PASSWORD)
    await prepare_login.login_page.click_submit()

    return prepare_login


@pytest_asyncio.fixture
async def prepare_checkout(prepare_login):

    prepare_checkout = prepare_login

    await prepare_checkout.products_page.open_check()
    await prepare_checkout.products_page.add_to_cart()
    await prepare_checkout.products_page.click_cart()

    await prepare_checkout.cart_page.open_check()
    await prepare_checkout.cart_page.click_checkout()

    await prepare_checkout.checkout_step_1_page.open_check()

    return prepare_checkout