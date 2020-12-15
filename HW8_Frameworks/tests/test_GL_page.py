import pytest

from pages.GL_page import (
    GLCareersPage,
    GLCareersResultPage,
)


def test_GL_page_search(browser):

    careersPage = GLCareersPage(browser)
    careersPage.open()
    careersPage.search_vacancy("QA")

    # resultPage = GLCareersResultPage(browser)
    # resultPage.open("QA")
    # print(resultPage.get_first())
