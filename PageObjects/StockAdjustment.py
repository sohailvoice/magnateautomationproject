import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.stock import StockTransferPage
import global_funcations1

@pytest.mark.usefixtures("setup")

class StockAdjustmentPage:
    def __init__(self, driver):
        self.driver = driver


        self.click_adjusment_Option=(By.XPATH,"//button[normalize-space()='Stock Adjustment']")
        self.click_new_icon=(By.XPATH,"//span[normalize-space()='New']")
        self.warehouse = (By.XPATH, "/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-inventory[1]/smacc-stock[1]/smacc-form-page[1]/s-page-wrapper[1]/form[1]/s-page-body[1]/s-container[1]/s-row[1]/s-col[3]/s-autocomplete[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        self.Adjustment_by = (By.XPATH, "//input[@placeholder='e.g. name or position']")
        self.Reference_number = (By.XPATH, "//input[@placeholder='Enter reference number']")
        self.Product1 = (By.XPATH, "//input[@class='form-control focusInput ng-star-inserted']")
        self.physical_quantity = (By.XPATH, "/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-inventory[1]/smacc-stock[1]/smacc-form-page[1]/s-page-wrapper[1]/form[1]/s-page-body[1]/s-container[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/s-form-input[1]/div[1]/input[1]")
        self.get_stock_value=(By.CSS_SELECTOR,"td[class='text-end'] div[class='grid-item-wrap'] span")
        self.click_enter_quantity=(By.CSS_SELECTOR,"div[class='input-group'] input[class='form-control ng-star-inserted']")
        self.enter_physical_quantity=(By.XPATH,"//input[@placeholder='Physical Quantity']")

    def click_stock_adjustment(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_adjusment_Option)
        ).click()

    def click_new_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_new_icon)
        ).click()

    def warehouse_select(self, warehouse):
        adjustment_warehouse = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.warehouse)
        )
        adjustment_warehouse.click()
        # adjustment_warehouse.clear()
        adjustment_warehouse.send_keys(warehouse)

    def enter_adjustment_by(self, warehouse2):
        adjustment_warehouse = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.Adjustment_by)
        )
        adjustment_warehouse.click()
        adjustment_warehouse.send_keys(warehouse2)

    def reference_number(self, referencenumber):
        adjustment_warehouse = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.Reference_number)
        )
        adjustment_warehouse.click()
        adjustment_warehouse.send_keys(referencenumber)


    def enter_product_name(self, product):
        adjustment_product_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.Product1)
        )
        adjustment_product_name.click()
        adjustment_product_name.send_keys(product)

    def enter_physical_quantity2(self):
        adjustment_physical_quantity2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.click_enter_quantity)
        )

        adjustment_physical_quantity2.click()
        adjustment_physical_quantity2.clear()


    def enter_physical_quantity(self,physicalqty):
       adjustment_physical_quantity = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.enter_physical_quantity)
    )
       adjustment_physical_quantity.send_keys(physicalqty)

    def get_availble_stock_qty(self):
         return self.driver.find_element(*self.get_stock_value).text  # Locate the element
         # Convert the text value to an integer and return



