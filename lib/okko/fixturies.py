import pytest
from lib.okko.okko_page import OkkoPage

@pytest.fixture
def okko_web_page(browser) -> OkkoPage:
    return OkkoPage(driver=browser)
