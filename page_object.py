from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage


class LoginPage(BasePage):

    URL = "https://loginpage.com"
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "button")

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.open_page(LoginPage.URL)

    def login(self, email, password):
        self.find_element(LoginPage.EMAIL_FIELD).send_keys(email)
        self.find_element(LoginPage.PASSWORD_FIELD).send_keys(password)
        self.click_element(LoginPage.LOGIN_BUTTON)
        return DashboardPage(self.browser)


class DashboardPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
