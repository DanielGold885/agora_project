import pytest
from utils.browser_managers.chrome_manager import ChromeManager
from pages.form_page import FormPage

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = ChromeManager().get_driver()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

@pytest.fixture
def form_page(driver):
    return FormPage(driver)
