import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC

import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.StockAdjustment import StockAdjustmentPage
import global_funcations1



@pytest.mark.usefixtures("setup")
class TestStockAdjustment:

    stock_warehouse = "Lahore"
    Adjustment_by = "Sohail Sagar"
    Reference_Number = "786"

    adjustment_product_name = "0058"
    physical_quantity =10



    def test_001(self, setup):
        lg = LoginPage(self.driver)
        db = DashboardPage(self.driver)
        time.sleep(1)
        # Enter username
        lg.input_user("sohail.915")
        time.sleep(1)
        # Enter password
        lg.input_password("12345678")
        time.sleep(1)
        # click login button
        lg.login_button()
        time.sleep(1)
        print("Login successfully")
        time.sleep(2)


        assert self.driver.current_url == "http://xsmacc7cloudx.dyndns.org:84/dashboard"

    def test_go_Stock_transfer_page(self):
        # Navigate to the stock transfer page
        global_funcations1.click_button(self.driver, "/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-sidebar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/button[1]/i[1]")
        time.sleep(1)
        global_funcations1.click_button(self.driver, "//button[normalize-space()='Stock']")
        # global_funcations1.click_button(self.driver, "//button[normalize-space()='Stock Adjustment']")
        # time.sleep(5)
    def test_create_stock_adjustment(self):
        stock_adjustment=StockAdjustmentPage(self.driver)

        # click Stock Adjustment Option
        stock_adjustment.click_stock_adjustment()
        time.sleep(1)
        # click new button on stock adjustment page
        stock_adjustment.click_new_button()

        # Select Warehosue on Adjustment Page
        stock_adjustment.warehouse_select(self.stock_warehouse)
        time.sleep(1)
        # Enter Reference number
        stock_adjustment.reference_number(self.Reference_Number)
        # Enter Adjustment
        stock_adjustment.enter_adjustment_by(self.Adjustment_by)

        # Enter first name
        stock_adjustment.enter_product_name(self.adjustment_product_name)
        time.sleep(1)
        stock_adjustment.enter_physical_quantity2()
        time.sleep(5)
        stock_adjustment.enter_physical_quantity(self.physical_quantity)
        # value = stock_adjustment.get_availble_stock_qty()
        # time.sleep(1)
        # Print the value to the console



