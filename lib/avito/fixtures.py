import pytest
from lib.avito.avito_page import AvitoPage


@pytest.fixture
def avito_web_page(browser) -> AvitoPage:
    return AvitoPage(driver=browser)