import time
from selenium.webdriver.common.by import By

import global_funcations1
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
import pytest
import allure
@pytest.mark.usefixtures("setup")
class TestLoging:


      def test_001(self,setup):
       for i in range(5):
        lg = LoginPage(self.driver)
        db = DashboardPage(self.driver)
        time.sleep(1)
        # Enter username
        lg.input_user("sohail.914")
        time.sleep(1)
        # Enter password
        lg.input_password("sohail@914")


        time.sleep(1)
        # click login button
        lg.login_button()
        time.sleep(2)
        print("login Succesfully ")
        time.sleep(2)
        # click Inventory Options
        global_funcations1.click_button(self.driver,"/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-sidebar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/button[1]/i[1]")
        time.sleep(60)
        # click Stock Option
        global_funcations1.click_button(self.driver,"//button[normalize-space()='Stock']")
        time.sleep(60)
        global_funcations1.click_button(self.driver,"//button[normalize-space()='Stock Transfer']")
        time.sleep(60)
        global_funcations1.click_button(self.driver,"//span[normalize-space()='New']")
        time.sleep(60)
        global_funcations1.click_button(self.driver, "//img[@src='../../../assets/img/logo.svg']")
        time.sleep(60)
        global_funcations1.click_button(self.driver,"/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-sidebar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/button[1]/i[1]")
        time.sleep(60)
        global_funcations1.click_button(self.driver, "//button[normalize-space()='Stock']")
        time.sleep(60)
        global_funcations1.click_button(self.driver, "//button[normalize-space()='Stock Transfer']")
        time.sleep(60)
        global_funcations1.click_button(self.driver, "//span[normalize-space()='New']")
        print(f"Login Attempt {i + 1} completed")





        # for i in range(10):  # Adjust the range for the number of iterations
        #
        #   if self.driver.current_url == "http://xsmacc7cloudx.dyndns.org:84/dashboard":
        #     assert True
        #   else:
        #     assert False
        #
        #   global_funcations1.click_button(self.driver,"/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-sidebar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/button[1]/i[1]")
        #   time.sleep(10)
        #   global_funcations1.click_button(By.XPATH, "//button[normalize-space()='Stock']")
        #   time.sleep(10)
        #   global_funcations1.click_button(By.XPATH,"//button[normalize-space()='Stock Location']")
        #   time.sleep(10)
        #   self.driver.refresh()
        #   print(f"Refreshing... {i + 1}")
        #   time.sleep(60)