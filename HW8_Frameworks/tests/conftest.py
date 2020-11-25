import json
import pytest

from selenium.webdriver import Chrome

CONFIG_PATH = "config/config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = "chrome"


@pytest.fixture(scope="session")
def config():
    # Read the JSON config file and return it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope="session")
def config_browser(config):
    # Validate and return the browser choice form the config data
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope="session")
def config_wait_time(config):
    # Validate and return the wait time form the config data
    return config["wait_time"] if "wait_time" in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == "chrome":
        driver = Chrome()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()