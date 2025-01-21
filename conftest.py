import pytest
from selenium import webdriver

from data import Urls

@pytest.fixture(params=['chrome', "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(Urls.MAIN_URL)
    yield driver
    driver.quit()
