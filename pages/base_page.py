from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        WebDriverWait(self.driver, 13).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def drag_and_drop(self, locator1, locator2):
        drag1 = self.find_element_with_wait(locator1)
        drag2 = self.find_element_with_wait(locator2)

        # без этого кода в firefox не работает перетаскивание
        self.driver.execute_script("""
                           var source = arguments[0];
                           var target = arguments[1];
                           var evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           source.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           source.dispatchEvent(evt);
                       """, drag1, drag2)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def wait_for_element_clickable(self, locator, timeout = 60):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

