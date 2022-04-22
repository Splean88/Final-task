# страница пользовательского профиля
from selenium.webdriver.common.by import By
from Locators3 import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.click_bottom_sing_in_xpath = Locators.click_buttom_sing_in_xpath
        self.click_forget_password_xpath = Locators.click_forget_password_xpath
        self.click_registration_xpath = Locators.click_registration_xpath
        self.click_main_label_Moscow_class_name = Locators.click_main_label_Moscow_class_name
        self.click_advanced_search_xpath = Locators.click_advanced_search_xpath
        self.click_contacts_xpath = Locators.click_contacts_xpath
        self.click_delivery_and_payment_xpath = Locators.click_delivery_and_payment_xpath
        self.click_privilege_xpath = Locators.click_privilege_xpath
        self.click_delivery_in_my_city_xpath = Locators.click_delivery_in_my_city_xpath
        self.click_our_projects_xpath = Locators.click_our_projects_xpath
        self.click_gold_savings_card_xpath = Locators.click_gold_savings_card_xpath
        self.click_news_and_events_class_name = Locators.click_news_and_events_class_name
        self.click_about_us_xpath = Locators.click_about_us_xpath
        self.click_my_favorites_xpath = Locators.click_my_favorites_xpath
        self.click_basket_xpath = Locators.click_basket_xpath
        self.click_button_basketBtnGo_xpath = Locators.click_button_basketBtnGo_xpath
        self.click_request_a_call_xpath = Locators.click_request_a_call_xpath
        self.click_close_request_a_call_xpath = Locators.click_close_request_a_call_xpath
        self.click_gratitudes_xpath = Locators.click_gratitudes_xpath
        self.click_my_cabinet_xpath = Locators.click_my_cabinet_xpath
        self.input_contact_info_message_name = Locators.input_contact_info_message_name
        self.click_bottom_save_contact_info_xpath = Locators.click_bottom_save_contact_info_xpath
        self.click_my_orders_xpath = Locators.click_my_orders_xpath
        self.click_discount_cards_xpath = Locators.click_discount_cards_xpath
        self.click_my_finance_xpath = Locators.click_my_finance_xpath
        self.click_my_digital_library_xpath = Locators.click_my_digital_library_xpath
        self.click_subscription_xpath = Locators.click_subscription_xpath
        self.click_change_password_xpath = Locators.click_change_password_xpath

        self.click_link_vk_xpath = Locators.click_link_vk_xpath
        self.click_link_twitter_xpath = Locators.click_link_twitter_xpath
        self.click_link_youtube_xpath = Locators.click_link_youtube_xpath
        self.click_link_telegram_bot_xpath = Locators.click_link_telegram_bot_xpath
        self.click_link_ok_xpath = Locators.click_link_ok_xpath
        self.click_link_yandex_zen_xpath = Locators.click_link_yandex_zen_xpath
        self.catalog_products_xpath = Locators.catalog_products_xpath
        self.click_telephone_number_class_name = Locators.click_telephone_number_class_name
        self.click_email_adress_class_name = Locators.click_email_adress_class_name


    def click_buttom_sing_in(self):
        self.driver.find_element(By.XPATH, self.click_bottom_sing_in_xpath).click()

    def click_forget_password(self):
        self.driver.find_element(By.XPATH, self.click_forget_password_xpath).click()

    def click_registration(self):
        self.driver.find_element(By.XPATH, self.click_registration_xpath).click()

    def click_main_label_Moscow(self):
        self.driver.find_element(By.CLASS_NAME, self.click_main_label_Moscow_class_name).click()

    def click_advanced_search(self):
        self.driver.find_element(By.XPATH, self.click_advanced_search_xpath).click()

    def click_contacts(self):
        self.driver.find_element(By.XPATH, self.click_contacts_xpath).click()

    def click_delivery_and_payment(self):
        self.driver.find_element(By.XPATH, self.click_delivery_and_payment_xpath).click()

    def click_delivery_in_my_city(self):
        self.driver.find_element(By.XPATH, self.click_delivery_in_my_city_xpath).click()

    def click_privilege(self):
        self.driver.find_element(By.XPATH, self.click_privilege_xpath).click()

    def click_gold_savings_card(self):
        self.driver.find_element(By.XPATH, self.click_gold_savings_card_xpath).click()

    def click_our_projects(self):
        self.driver.find_element(By.XPATH, self.click_our_projects_xpath).click()

    def click_news_and_events(self):
        self.driver.find_element(By.CLASS_NAME, self.click_news_and_events_class_name).click()

    def click_about_us(self):
        self.driver.find_element(By.XPATH, self.click_about_us_xpath).click()

    def click_my_favorites(self):
        self.driver.find_element(By.XPATH, self.click_my_favorites_xpath).click()

    def click_basket(self):
        self.driver.find_element(By.XPATH, self.click_basket_xpath).click()

    def click_button_basketBtnGo(self):
        self.driver.find_element(By.XPATH, self.click_button_basketBtnGo_xpath).is_displayed()

    def click_request_a_call(self):
        self.driver.find_element(By.XPATH, self.click_request_a_call_xpath).click()

    def click_close_request_a_call(self):
        self.driver.find_element(By.XPATH, self.click_close_request_a_call_xpath).click()

    def click_gratitudes(self):
        self.driver.find_element(By.XPATH, self.click_gratitudes_xpath).click()

    def click_my_cabinet(self):
        self.driver.find_element(By.XPATH, self.click_my_cabinet_xpath).click()

    def input_contact_info_message(self):
        self.driver.find_element(By.NAME, self.input_contact_info_message_name).click()

    def click_bottom_save_contact_info(self):
        self.driver.find_element(By.XPATH, self.click_bottom_save_contact_info_xpath).click()

    def click_my_orders(self):
        self.driver.find_element(By.XPATH, self.click_my_orders_xpath).click()

    def click_discount_cards(self):
        self.driver.find_element(By.XPATH, self.click_discount_cards_xpath).click()

    def click_my_finance(self):
        self.driver.find_element(By.XPATH, self.click_my_finance_xpath).click()

    def click_my_digital_library(self):
        self.driver.find_element(By.XPATH, self.click_my_digital_library_xpath).click()

    def click_subscription(self):
        self.driver.find_element(By.XPATH, self.click_subscription_xpath).click()

    def click_change_password(self):
        self.driver.find_element(By.XPATH, self.click_change_password_xpath).click()




    def click_link_vk(self):
        self.driver.find_element(By.XPATH, self.click_link_vk_xpath).click()

    def click_link_twitter(self):
        self.driver.find_element(By.XPATH, self.click_link_twitter_xpath).click()

    def click_link_youtube(self):
        self.driver.find_element(By.XPATH, self.click_link_youtube_xpath).click()

    def click_link_telegram_bot(self):
        self.driver.find_element(By.XPATH, self.click_link_telegram_bot_xpath).click()

    def click_link_ok(self):
        self.driver.find_element(By.XPATH, self.click_link_ok_xpath).click()

    def click_link_yandex_zen(self):
        self.driver.find_element(By.XPATH, self.click_link_yandex_zen_xpath).click()

    def catalog_products(self):
        self.driver.find_element(By.XPATH, self.catalog_products_xpath).is_displayed()

    def click_telephone_number(self):
        self.driver.find_element(By.CLASS_NAME, self.click_telephone_number_class_name).click()

    def click_email_adress(self):
        self.driver.find_element(By.CLASS_NAME, self.click_email_adress_class_name).click()
