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

class TransactionVewPage:
    def __init__(self, driver):
        self.driver = driver


        self.financial_module_field=(By.CSS_SELECTOR,"button[popoverclass='menu-popover'] i[class='icon-menu-finance']")
        self.transaction_option=(By.XPATH,"/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-sidebar[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/li[3]/button[1]")
        self.transaction_view = (By.CSS_SELECTOR, "body > smacc-layouts:nth-child(2) > div:nth-child(3) > smacc-sidebar:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > button:nth-child(1)")
        self.financial_account_option=(By.CSS_SELECTOR,"ul[class='nav nav-tabs ng-star-inserted'] li:nth-child(1) div:nth-child(1)")
        self.click_last_icon=(By.CSS_SELECTOR,"//i[@class='icon-grid-chevron-last']")
        self.search_document=(By.CSS_SELECTOR,"input[placeholder='Search ...']")

    def click_financial_module(self):
        return self.driver.find_element(*self.financial_module_field).click()

    def click_transaction_icon(self):
        return self.driver.find_element(*self.transaction_option).click()

    def click_search(self):
        wait = WebDriverWait(self.driver, 10)
        search_element = wait.until(EC.element_to_be_clickable(self.search_document))
        search_element.click()
    #
    # def click_transaction_icon(self):
    #  button = WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-anchor']"))
    # )
    #  button.click()

    def click_transaction_page(self):
        return self.driver.find_element(*self.transaction_view).click()
    def click_transaction_account_page(self):
        return self.driver.find_element(*self.financial_account_option).click()
    def click_last_document(self):
        return self.driver.find_element(*self.click_last_icon).click()
    # def click_search(self):
    #     return self.driver.find_element(*self.search_document).click()