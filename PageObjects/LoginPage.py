from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        # Initialize the driver attribute
        self.texbox_username_xpath = "//input[@placeholder='Username']"
        self.texbox_password_xpath = "//input[@placeholder='Password']"
        self.button_login_xpath = "//button[normalize-space()='Login']"

    def input_user(self, username):

         self.driver.find_element(By.XPATH, self.texbox_username_xpath).send_keys(username)


    def input_password(self, password):
        self.driver.find_element(By.XPATH, self.texbox_password_xpath).send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()





