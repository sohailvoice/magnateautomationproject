#
import time
import pytest
import allure
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_001(self):
        self.driver.implicitly_wait(10)
        lg = LoginPage(self.driver)

        try:
            # Enter Username
            lg.input_user("m.sohail@arabsea.com")  # Replace with actual username

            # Enter Password
            lg.input_password("12345678")  # Replace with actual password

             # Click Login Button
            lg.login_button()
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Button Clicked",
                          attachment_type=allure.attachment_type.PNG)
            print("Login Button Clicked")
            time.sleep(2)

            # Verify Login
    # Wait for login to process and page to load
            assert "dashboard" in self.driver.current_url.lower(), "Login failed or incorrect URL"
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Successful",
                          attachment_type=allure.attachment_type.PNG)

            time.sleep(10)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error",
                          attachment_type=allure.attachment_type.PNG)
            print(f"Test failed: {e}")
            time.sleep(10)


# #
#     def test_002(self):
#         lg = LoginPage(self.driver)
#         db = DashboardPage(self.driver)
#         time.sleep(2)
#         # Enter Invalid username
#         lg.input_user("sohail.9044")
#         # Enter Password
#         lg.input_password("admin123")
#         # click login button
#         lg.login_button()
#         time.sleep(2)
#         if self.driver.current_url != "http://xsmacc7cloudx.dyndns.org:84/dashboard":
#             assert True
#         else:
#             assert False


#     def test_003(self):
#         lg=Login(self.driver)
#         db = DashBoard(self.driver)
#         time.sleep(2)
#         # Enter valid username
#         lg.input_user("sohail.904")
#         # Enter Invalid password
#         lg.input_password("Sohail@1234")
#         # click login button
#         lg.login_button()
#         time.sleep(2)
#         if self.driver.current_url != "http://xsmacc7cloudx.dyndns.org:84/dashboard":
#             assert True
#         else:
#             assert False
#
#     def test_004(self):
#         lg=Login(self.driver)
#         db = DashBoard(self.driver)
#         time.sleep(2)
#         # Enter invalid username
#         lg.input_user("")
#         # Enter invalid password
#         lg.input_password("")
#         # click login button
#         lg.login_button()
#
#         time.sleep(5)
#         if self.driver.current_url != "http://xsmacc7cloudx.dyndns.org:84/dashboard":
#             assert True
#         else:
#             assert False#





