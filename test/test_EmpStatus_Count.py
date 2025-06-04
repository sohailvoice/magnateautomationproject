# import time
# from selenium.webdriver.common.by import By
# from PageObjects.LoginPage import Login
# from PageObjects.DashboardPage import DashBoard
# import pytest
#
# @pytest.mark.usefixtures("setup")
# class TestLoging:
#     def test_t1(self):
#         lg = Login(self.driver)
#         db = DashBoard(self.driver)
#         time.sleep(3)
#         lg.input_user("sohail.904")
#         lg.input_password("Sohail@123")
#         lg.login_button()
#         time.sleep(30)
#         if self.driver.current_url == "http://xsmacc7cloudx.dyndns.org:84/dashboard":
#             assert True
#         else:
#             assert False
#
