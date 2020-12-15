from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from pages.base_page import BasePage


class GoogleSearchPage(BasePage):
    URL = "https://www.google.com/"
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.open_page(GoogleSearchPage.URL)

    def search(self, phrase):
        self.find_an_element(GoogleSearchPage.SEARCH_FIELD).send_keys(phrase)
        self.click_element(GoogleSearchPage.SEARCH_BUTTON)

        return GoogleSearchResultPage(self.browser)


class GoogleSearchResultPage(BasePage):

    RESULT = (By.PARTIAL_LINK_TEXT, "pypi.org")

    def __init__(self, browser):
        super().__init__(browser)

    def search_click_result(self):
        return self.click_element(GoogleSearchResultPage.RESULT)


class PypiPage(BasePage):

    SEARCH_PROJECTS_FIELD = (By.ID, "search")
    SEARCH_FORM_BUTTON = (By.CLASS_NAME, "search-form__button")

    def __init__(self, browser):
        super().__init__(browser)

    def search(self, phrase):
        self.find_an_element(PypiPage.SEARCH_PROJECTS_FIELD).send_keys(phrase)
        self.click_element(PypiPage.SEARCH_FORM_BUTTON)

        return PypiResultPage(self.browser)


class PypiResultPage(BasePage):

    RESULTS = (By.CLASS_NAME, "package-snippet")

    def __init__(self, browser):
        super().__init__(browser)

    def get_second(self):
        return self.click_element_from_list(PypiResultPage.RESULTS, 1)

    def get_result(self, number):
        return self.click_element_from_list(PypiResultPage.RESULTS, number)
