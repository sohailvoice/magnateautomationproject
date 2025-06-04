import pytest

@pytest.fixture(scope="class")
def setup(request):
    from selenium import webdriver
    request.cls.driver= webdriver.Firefox()
    # request.cls.driver=webdriver.firefox()
    request.cls.driver.maximize_window()
    request.cls.driver.get("http://xsmacc7cloudx.dyndns.org:86/login")
    yield
    request.cls.driver.quit()