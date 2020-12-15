from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage


class GLCareersPage(BasePage):
    URL = "https://www.globallogic.com/ua/careers/"

    SEARCH_FIELD = (By.ID, "by_keyword")
    SEARCH_BUTTON = (
        By.XPATH,
        '//*[@id="hero"]/div/div/div/div/div/div/div[1]/form/div/button',
    )
    COOKIE_ALLOW_ALL_BUTTON = (
        By.ID,
        "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll",
    )

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.open_page(GLCareersPage.URL)
        self.click_element(GLCareersPage.COOKIE_ALLOW_ALL_BUTTON)

    def search_vacancy(self, vacancy, enter=False):
        self.find_an_element(GLCareersPage.SEARCH_FIELD).send_keys(vacancy)
        self.click_element(GLCareersPage.SEARCH_BUTTON)

        return GLCareersResultPage(self.browser)


class GLCareersResultPage(BasePage):

    FIRST_RESULT = (By.CLASS_NAME, "mb-0")

    def __init__(self, browser):
        super().__init__(browser)

    def open(self, by_keyword=None):
        self.browser.get(
            f"https://www.globallogic.com/ua/career-search-page/?keywords={by_keyword}&experience=&locations=&c="
        )
        return True

    def get_first(self):
        first_result = self.find_an_element(GLCareersResultPage.FIRST_RESULT)
        return first_result.text


driver = webdriver.Chrome()

# careersPage = GLCareersPage(driver)
# careersPage.open()
# careersPage.search_vacancy("QA")

resultPage = GLCareersResultPage(driver)
resultPage.open("QA")
print(resultPage.get_first())
driver.quit()
