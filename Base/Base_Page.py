
from playwright.async_api import expect

class BasePage:

    def __init__(self, page):
        self.page = page
        self.expect = expect

    async def open(self):
        await self.page.goto(self.PAGE_URL)


    async def open_check(self):
        await self.page.wait_for_url(self.PAGE_URL)