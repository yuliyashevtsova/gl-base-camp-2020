import pytest

from pages.google_page import (
    GoogleSearchPage,
    GoogleSearchResultPage,
    PypiPage,
    PypiResultPage,
)


def test_google_search(browser):
    PHRASE_1 = "selenium install ubuntu python"
    PHRASE_2 = "selenium library"

    google = GoogleSearchPage(browser)
    google.open()
    google.search(PHRASE_1)
    result = GoogleSearchResultPage(browser)
    result.search_click_result()
    pypi = PypiPage(browser)
    pypi.search(PHRASE_2)
    pypi_result = PypiResultPage(browser)
    pypi_result.get_second()
