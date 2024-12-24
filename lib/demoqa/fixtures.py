import pytest
from lib.demoqa.pages.demoqa_page import DemoQaPage
from lib.demoqa.pages.demoqa_chekbox_page import DemoQaCheckBoxPage
from lib.demoqa.pages.demoqa_uploaddownlad_page import DemoQaUploadDownloadPage


@pytest.fixture
def demoqa_page(browser) -> DemoQaPage:
    return DemoQaPage(driver=browser)

@pytest.fixture
def demoqa_page_checkbox(browser) -> DemoQaCheckBoxPage:
    return DemoQaCheckBoxPage(driver=browser)

@pytest.fixture
def demoqa_page_upload_download(browser) -> DemoQaUploadDownloadPage:
    return DemoQaUploadDownloadPage(driver=browser)
