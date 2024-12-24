import pytest
from lib.gost_team.pages.gost_team_page import GostTeamPage


@pytest.fixture
def gost_team_page(browser) -> GostTeamPage:
    return GostTeamPage(driver=browser)
