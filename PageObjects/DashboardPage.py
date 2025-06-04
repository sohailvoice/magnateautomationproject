# from idlelib import browser
#
# from selenium.webdriver.common.by import By
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class DashBoard:
#     def __init__(self, driver):
#         self.driver = driver
#         self.text_welcome_message_xpath = "//li[@class='breadcrumb-item ng-star-inserted active']"
#         self.click_adming_xpath="//a[@class='oxd-main-menu-item active']"
#         self.click_job_xpath="//span[normalize-space()='Job']"
#         self.empolyee_status_xpath="//a[normalize-space()='Employment Status']"
#
#     def welcome_message(self):
#         return self.driver.find_element(By.XPATH, self.text_welcome_message_xpath).text
#
#
#
#
#
#
#     def click_admin(self):
#         self.driver.find_element(By.XPATH, self.click_adming_xpath).click()
#     def click_job(self):
#         self.driver.find_element(By.XPATH, self.click_job_xpath).click()
from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.dashboard_heading = (By.XPATH, "//li[@class='breadcrumb-item ng-star-inserted active']")
        self.stock_transfer_menu = (By.ID, "stockTransferMenu")

    # Actions
    def get_dashboard_heading(self):
        return self.driver.find_element(*self.dashboard_heading).text

    def navigate_to_stock_transfer(self):
        self.driver.find_element(*self.stock_transfer_menu).click()
