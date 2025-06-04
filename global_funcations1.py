import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging

def click_button(driver,xpath):
    button=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    button.click()
def enter_button(driver,xpath):
    Source_Warehouse = "lahore"
    button2=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    button2.click()
    button2.send_keys(Source_Warehouse,Keys.ENTER)