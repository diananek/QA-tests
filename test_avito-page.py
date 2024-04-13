from playwright.sync_api import Page, Playwright, sync_playwright
import pytest
import json

URL = "https://www.avito.ru/avito-care/eco-impact"

@pytest.fixture(scope="module")
def browser_chromium():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        yield browser
        browser.close()
@pytest.fixture(scope="module")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="module")
def test_data():
    f = open('test_data_base.json')
    data = json.load(f)
    yield data
    f.close()

def test_open_page_non_autorized(page: Page, context):
    page = context.new_page()
    page.goto(URL)
    page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_1.1.png")

def test_open_page_non_autorized_click_autorize_btn(page: Page, context):
    page = context.new_page()
    page.goto(URL)
    page.get_by_role("button", name="Авторизоваться").click()

    new_page = context.wait_for_event('page')
    new_page.bring_to_front()
    new_page.wait_for_load_state()
    new_page.screenshot(path='output/test_1.2.png', full_page=True)

class TestsCO2Counter():
    def test_negative_value(self, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["co2"] = -1
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)

        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_2.1.png")
    def test_value_0(self, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["co2"] = 0
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)

        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_2.2.png")
    def test_value_1(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["co2"] = 1
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_2.3.png")
    def test_value_999(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["co2"] = 999
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)

        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_2.4.png")
    def test_value_1000(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["co2"] = 1000
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_2.5.png")
    def test_value_1001(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["co2"] = 1001
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_2.6.png")

class TestsWaterCounter():
    def test_negative_value(self, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["water"] = -1
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_3.1.png")
    def test_value_0(self, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["water"] = 0
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)

        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_3.2.png")
    def test_value_1(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["water"] = 1
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_3.3.png")
    def test_value_999(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["water"] = 999
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)

        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_3.4.png")
    def test_value_1000(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["water"] = 1000
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_3.5.png")
    def test_value_1001(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["water"] = 1001
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_3.6.png")
class TestsEnergyCounter():
    def test_negative_value(self, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["energy"] = -1
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)

        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_4.1.png")
    def test_value_0(self, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["energy"] = 0
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)

        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_4.2.png")
    def test_value_1(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["energy"] = 1
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_4.3.png")
    def test_value_999(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["energy"] = 999
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)

        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_4.4.png")
    def test_value_1000(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["energy"] = 1000
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_4.5.png")
    def test_value_1001(self, page: Page, test_data, context):
        page = context.new_page()
        test_data["result"]["blocks"]["personalImpact"]["data"]["energy"] = 1001
        page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", lambda route: route.fulfill(
            content_type="application/json",
            body=json.dumps(test_data)  
        ))
        page.goto(URL)
        page.locator(".desktop-wrapper-OutiE").screenshot(path="output/test_4.6.png")

    
    


