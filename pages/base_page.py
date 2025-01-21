from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def click_to_element(self, locator):
        button = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", button)

    def current_url(self):
        return self.driver.current_url

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locator))
        return self.driver.find_element(*locator)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def drag_and_drop(self, locator1, locator2):
        drag1 = self.find_element_with_wait(locator1)
        drag2 = self.find_element_with_wait(locator2)
        ActionChains(self.driver).drag_and_drop(drag1, drag2).perform()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

