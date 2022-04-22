# АВТОРИЗАЦИЯ
from selenium.webdriver.common.by import By
from Locators3 import Locators


class LoginPage:

    def __init__(self, driver):

        self.driver = driver
        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_xpath = Locators.login_button_xpath
        self.invalidUsername_xpath = Locators.invalidUsername_xpath
        self.invalidPassword_xpath = Locators.invalidPassword_xpath
        self.invalidUsernameAndPassword_xpath = Locators.invalidUsernameAndPassword_xpath


    def enter_username(self, username):

        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)


    def enter_password(self, password):

        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)


    def click_login(self):

        self.driver.find_element(By.XPATH, self.login_button_xpath).click()


    def check_invalid_username(self):

        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.XPATH, self.invalidUsername_xpath)


