# # pytest_plugins: list[str] = [
# #     'conftests.sohail'
# # ]
#
# import pytest
#
# @pytest.fixture(scope="class")
# def setup(request):
#     from selenium import webdriver
#     options = webdriver.ChromeOptions()
#     options.add_argument("--ignore-certificate-error")
#     options.add_argument("--ignore-ssl-errors")
#     # request.cls.driver= webdriver.Chrome()
#     # request.cls.driver=webdriver.firefox()
#     request.cls.driver.maximize_window()
#     request.cls.driver.get("http://xsmacc7cloudx.dyndns.org:84/login")
#     yield
#     request.cls.driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.accept_insecure_certs = True  # Allow insecure SSL certificates
    driver = webdriver.Firefox(options=options)  # Use Firefox WebDriver
    driver.maximize_window()
    driver.get("http://xsmacc7cloudx.dyndns.org:84/login")
    request.cls.driver = driver
    yield
    # Your target URL

    driver.quit()


