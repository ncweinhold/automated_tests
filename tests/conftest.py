import pytest

from helpers.yaml_helpers import read_yaml_file
from helpers.paths import ENVS

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def pytest_addoption(parser):
    parser.addoption(
        "--browser", dest="browser", action="store", default="chrome", help="Set the browser to use for the tests."
    )

def _provision_chrome():
    return webdriver.Chrome()

def _provision_firefox():
    capabilities = DesiredCapabilities().FIREFOX
    return webdriver.Firefox(capabilities=capabilities)

def _provision_safari():
    return webdriver.Safari()

@pytest.fixture(scope='session', autouse=True)
def driver(request):
    browsers = {
        'chrome': _provision_chrome,
        'firefox': _provision_firefox,
        'safari': _provision_safari
    }
    browser = request.config.getoption('browser')
    _driver = browsers[browser]()
    yield _driver
    _driver.quit()

@pytest.fixture(scope='session', autouse=True)
def env():
    yield read_yaml_file(ENVS)