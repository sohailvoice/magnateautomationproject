import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StockTransferPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.Inventory_option = (By.XPATH, "//button[@popoverclass='menu-popover']//i[@class='icon-menu-inventory']")
        self.source_location_dropdown = (By.XPATH, "//s-col[4]//s-autocomplete[1]//div[1]//div[1]//div[1]//div[1]//input[1]")
        self.destination_location_dropdown = (By.XPATH, "//s-autocomplete[@class='form-group ng-untouched ng-pristine ng-invalid']//input[@placeholder='Search by code or name']")
        self.item_input = (By.XPATH, "//s-autocomplete[@class='form-group ng-untouched ng-pristine ng-valid']//input[@placeholder='Search by code or name']")
        self.quantity_input = (By.XPATH, "//input[@placeholder='Quantity']")
        self.stock_value=(By.XPATH,"/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-inventory[1]/smacc-stock[1]/smacc-form-page[1]/s-page-wrapper[1]/form[1]/s-page-body[1]/s-container[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/s-form-input-group[1]/div[1]/div[1]/div[1]/span[1]")
        self.transfer_button = (By.XPATH, "//span[normalize-space()='Save']")
        self.click_blank_space=(By.XPATH,"//s-row[1]")
        self.calendar_date=(By.XPATH,"//input[@id='dateformat']")
        self.value_locator = (By.XPATH, "(//input[@value='Lahore'])[1]")
        self.scrol_by=(By.XPATH,"/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-inventory[1]/smacc-stock[1]/smacc-form-page[1]/s-page-wrapper[1]/form[1]/s-page-body[1]/s-container[1]/div[1]/div[1]/div[1]/table[1]/tfoot[1]/tr[1]/td[4]/span[1]")
        self.get_price_value_field=(By.CSS_SELECTOR,"body > smacc-layouts:nth-child(2) > div:nth-child(3) > smacc-inventory:nth-child(5) > smacc-stock:nth-child(2) > smacc-form-page:nth-child(2) > s-page-wrapper:nth-child(1) > form:nth-child(2) > s-page-body:nth-child(1) > s-container:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
        self.get_transfer_stock_document_number=(By.XPATH,"//tbody/tr[1]/td[1]/div[1]")
        self.click_Finanacial_icon =(By.CSS_SELECTOR,"button[popoverclass='menu-popover'] i[class='icon-menu-finance']")
        self.view=(By.XPATH,"//tr[@class='last bg-white']/td[2]/div[@class='grid-icon-box float-end']")
        self.debit=(By.CSS_SELECTOR,"tfoot td:nth-child(2) div:nth-child(1) span:nth-child(1)")
        self.credit = (By.CSS_SELECTOR, "tfoot td:nth-child(2) div:nth-child(1) span:nth-child(1)")
        self.click_plus_icon=(By.CSS_SELECTOR,".icon-plus")
        self.item_input2 = (By.CSS_SELECTOR,".form-control.focusInput.ng-star-inserted")
        self.quantity_input2 = (By.XPATH, "tr[class='ng-pristine ng-invalid ng-star-inserted ng-touched'] input[placeholder='Quantity']")
    def go_to_inventory(self):
        self.driver.find_element(*self.Inventory_option).click()

    def calendar_date(self):
        self.driver.find_element(*self.calendar_date).click()



        # calendar_icon.send_keys(Keys.ENTER)

    def select_source_location(self, location):
        dropdown = self.driver.find_element(*self.source_location_dropdown)
        dropdown.click()
        dropdown.send_keys(location)

    def select_destination_location(self, location2):
        dropdown2 = self.driver.find_element(*self.destination_location_dropdown)
        dropdown2.click()
        dropdown2.send_keys(location2)

    def enter_item(self, item):
        dropdown3=self.driver.find_element(*self.item_input)
        dropdown3.click()
        dropdown3.send_keys(item)

    def enter_item2(self, item):
        dropdown3 = self.driver.find_element(*self.item_input2)
        dropdown3.click()
        dropdown3.send_keys(item)


    def enter_quantity(self, quantity):
        product_qty=self.driver.find_element(*self.quantity_input)
        # product_qty.click()
        product_qty.send_keys(quantity)
        product_qty.clear()
        product_qty.send_keys(quantity)

    def enter_quantity2(self, quantity):
        product_qty = self.driver.find_element(*self.quantity_input2)
        # product_qty.click()
        product_qty.send_keys(quantity)
        product_qty.clear()
        product_qty.send_keys(quantity)

    def get_price_value(self):
        return self.driver.find_element(*self.get_price_value_field).text

    def get_value(self):
        # Retrieve text or value from the element
        return self.driver.find_element(*self.value_locator).text
    def get_success_stock(self):
        return self.driver.find_element(*self.stock_value).text
    def click_transfer(self):
        self.driver.find_element(*self.transfer_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text

    def click_space(self):
        return self.driver.find_element(*self.click_blank_space).click()
    def get_stock_transfter_number(self):
        return self.driver.find_element(*self.get_transfer_stock_document_number).click()
    def scrol_view(self):
        return self.driver.find_element(*self.view).click()
    def get_debit_value(self):
        return self.driver.find_element(*self.debit).text
    def get_credit_value(self):
        return self.driver.find_element(*self.credit).text

    def click_plus_icon(self):
        self.driver.find_element(*self.click_plus_icon).click()
















