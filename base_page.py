from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self, url):
        self.browser.get(url)

    def find_an_element(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((locator))
            )
            return self.browser.find_element(*locator)
        except TimeoutException:
            self.browser.quit()

    def find_elements(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located((locator))
            )
            return self.browser.find_elements(*locator)
        except TimeoutException:
            self.browser.quit()

    def click_element(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((locator))
            )
            self.browser.find_element(*locator).click()
        except TimeoutException:
            self.browser.quit()

    def click_element_from_list(
        self,
        locator,
        number,
        timeout=10,
    ):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located((locator))
            )
            list = self.browser.find_elements(*locator)
            return list[number].click()
        except TimeoutException:
            self.browser.quit()
