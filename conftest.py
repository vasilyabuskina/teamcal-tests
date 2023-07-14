import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = 'https://id.teamcal.ai/id/go/qaintern#'


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1200,800")

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()

