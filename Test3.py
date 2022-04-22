#  python -m pytest -v  --driver Chrome --driver-path C:\Users\antoo\PycharmProjects\pythonProject7END\chromedriver.exe Test3.py

from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from LoginPage3 import LoginPage
from HomePages3 import HomePage


class TestUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # СОЗДАЕМ НОВУЮ СЕССИЮ ДЛЯ CHROME

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_01_click_bottom_sing_in(self):  # "Проверка кликабельности кнопки "Войти""
        driver: WebDriver = self.driver
        driver.get('https://www.moscowbooks.ru')
        homepage = HomePage(driver)
        homepage.click_buttom_sing_in()
        driver.find_element(By.XPATH, '//*[@id="top"]/div[1]/div[1]/div[1]/ul[2]/li[1]/a[1]').click()

    def test_02_invalid_username(self):  # НЕГАТИВНЫЙ ТЕСТ "Ввод неправильного логина"
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username('Splean888@mail.ru')
        login.enter_password('Splean88')
        login.check_invalid_username()
        self.driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="popup-cart-auth"]/form/div[3]/button').is_displayed()

    def test_03_click_forget_password(self):  # "Проверка кликабельности 'Забыли пароль'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_forget_password()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="popup-cart-auth"]/form/span[3]/a').get_attribute('href')

    def test_04_email_input_line(self):  # "Проверка наличия строки ввода email для восстановления пароля"
        driver = self.driver
        driver.find_element(By.ID, 'Email').is_displayed()

    def test_05_click_registration(self):  # "Проверка кликабельности кнопки "Регистрация""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_registration()
        time.sleep(5)
        # driver.find_element(By.CLASS_NAME, 'header__top__auth__item__link auth_link_login').click()
        driver.find_element(By.XPATH, '//*[@id="top"]/div[1]/div/div/ul[2]/li[2]/a').click()

    def test_06_password_input_line(self):  # "Проверка наличия строки ввода пароля при регистрации"
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="Password"]').is_displayed()

    def test_07_click_main_label_Moscow(self):  # "Проверка кликабельности кнопки 'Москва' и перехода на главную
        # страницу"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_main_label_Moscow()
        time.sleep(10)
        driver.find_element(By.CLASS_NAME, 'header__main__logo').click()

    def test_08_search_bar(self):  # "Проверка наличия строки поиска на сайте"
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="mb_hdr"]/div/div/div/div/div[1]/div/form/input[1]').is_displayed()

    def test_09_button_find_search_bar(self):  # "Проверка наличия кнопки 'Искать' для строки поиска"
        driver = self.driver
        driver.find_element(By.CLASS_NAME, 'header__main__search__form__submit').is_displayed()

    def test_10_click_advanced_search(self):  # "Проверка кликабельности кнопки 'Расширенный поиск'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_advanced_search()
        time.sleep(5)
        #driver.find_element(By.CLASS_NAME, 'header__main__search__link').click()
        driver.find_element(By.XPATH, '//*[@id="mb_hdr"]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]').click()
    # тест, то проходит, то падает... Локатор не меняется.

    def test_11_advanced_search_auther(self):  # "Проверка наличия ввода автора для расширенного поиска"
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="Author"]').is_displayed()

    def test_12_click_contacts(self):  # "Проверка кликабельности кнопки 'Контакты'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_contacts()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[1]/div/div/ul[1]/li[6]/a').click()
        time.sleep(5)

    def test_13_click_delivery_and_payment(self):  # "Проверка кликабельности кнопки 'Доставка и оплата'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_delivery_and_payment()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[1]/div/div/ul[1]/li[5]/a').click()

    def test_14_click_delivery_in_my_city(self):  # "Проверка кликабельности кнопки 'Доставка в мой город'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_delivery_in_my_city()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div/div[3]/div[2]/article/div[2]/div[2]/div/a').click()

    def test_15_click_privilege(self):  # "Проверка кликабельности кнопки 'Привилегии'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_privilege()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[1]/div/div/ul[1]/li[4]/a').click()

    def test_16_click_gold_savings_card(self):  # "Проверка кликабельности 'Золотая накопительная карта'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_gold_savings_card()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div/div[3]/div[2]/article/p[2]/strong/a/img').click()

    def test_17_click_our_projects(self):  # "Проверка кликабельности кнопки 'Наши проекты'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_our_projects()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[1]/div/div/ul[1]/li[3]/a').click()

    def test_18_click_news_and_events(self):  # "Проверка кликабельности 'Новости и мероприятия'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_news_and_events()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'header__top__menu__item__link').click()

    def test_19_click_about_us(self):  # "Проверка кликабельности 'О нас'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_about_us()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[1]/div/div/ul[1]/li[1]/a').click()

    def test_20_click_bottom_sing_in(self):  # "Проверка кликабельности кнопки "Войти""
        driver: WebDriver = self.driver
        driver.get('https://www.moscowbooks.ru')
        homepage = HomePage(driver)
        homepage.click_buttom_sing_in()
        driver.find_element(By.XPATH, '//*[@id="top"]/div[1]/div[1]/div[1]/ul[2]/li[1]/a[1]').click()

    def test_21_login_valid(self):  # "Ввод верного логина и пароля"
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username('Splean88@mail.ru')
        login.enter_password('Splean88')
        login.click_login()
        self.driver.implicitly_wait(10)

    def test_22_click_my_favorites(self):  # "Проверка кликабельности кнопки 'Избранное'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_my_favorites()
        self.driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//*[@id="mb_hdr"]/div/div/div/div/div[2]/a[2]').click()

    def test_23_delete_my_favorites(self):  # "Наличие кнопки 'х' для удаления товара из 'Избранного'"
        driver = self.driver
        self.driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//*[@id="div_fav_1103391_0"]/div/div/div[1]/div').is_displayed()

    def test_24_click_basket(self):  # "Проверка кликабельности кнопки 'Корзина'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_basket()
        self.driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//*[@id="mb_hdr"]/div/div/div/div/div[2]/a[1]').click()

    def test_25_more_buys(self):  # "Наличие кнопки '+' для увеличения количества товара в корзине"
        driver = self.driver
        time.sleep(5)
        #driver.find_element(By.CLASS_NAME, 'amount-form__control amount-form__control_dec js-amount-control').click()
        #driver.find_element(By.NAME, 'action_plus').click()
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div[1]/form/div[2]/div[1]/div[1]/div[2]/div[4]/div/div/button[2]').click()
    #  тест периодически падает из-за того, что меняется локатор: то он находит по class_name, то по name, то по xpath

    def test_26_less_buys(self):  # "Наличие кнопки '-' для уменьшения количества товара в корзине"
        driver = self.driver
        time.sleep(5)
        #driver.find_element(By.CLASS_NAME, 'amount-form__control amount-form__control_inc js-amount-control').click()
        #driver.find_element(By.NAME, 'action_minus').click()
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div[1]/form/div[2]/div[1]/div[1]/div[2]/div[4]/div/div/button[1]').click()
    #  тест периодически падает из-за того, что меняется локатор: то он находит по class_name, то по name, то по xpath

    def test_27_delete_buys(self):  # "Наличие кнопки 'х' для удаления товара из корзины"
        driver = self.driver
        self.driver.implicitly_wait(5)
        #driver.find_element(By.CLASS_NAME, 'cart__item-delete icon-close').click()
        #driver.find_element(By.NAME, 'action_delete').click()
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div[1]/form/div[2]/div[1]/button[2]').click()
    #  тест периодически падает из-за того, что меняется локатор: то он находит по class_name, то по name, то по xpath

    def test_28_click_button_basketBtnGo(self):  # "Проверка наличия кнопки в корзине 'Оформить заказ'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_button_basketBtnGo()
        self.driver.implicitly_wait(5)
        #driver.find_element(By.CLASS_NAME, 'cart__button button button_primary button_lg js-progress').click()
        driver.find_element(By.XPATH, '//*[@id="button_next"]').click()

    def test_29_click_gratitudes(self):  # "Проверка кликабельности кнопки 'Отзывы"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_gratitudes()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div/div[1]/div/div/div[1]/ul/li[5]/a').click()
        #driver.find_element(By.CLASS_NAME, 'subnav-footer__link link-white link-underlined').click()

    def test_30_click_my_cabinet(self):  # "Проверка кликабельности кнопки "Войти""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_my_cabinet()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="logoutform"]/ul/li[1]/a').click()

    def test_31_input_contact_info_message(self):  # "Возможность ввода контактной информации в моем профиле"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.input_contact_info_message()
        driver.find_element(By.NAME, 'FirstName').click()

    def test_32_click_bottom_save_contact_info(self):  # "Проверка кликабельности кнопки "Сохранить" в моем профиле"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_bottom_save_contact_info()
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div/div[3]/div[2]/div/form/div[16]/button').click()

    def test_33_click_my_orders(self):  # "Проверка кликабельности кнопки 'Мои заказы'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_my_orders()
        self.driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/ul/li[5]/a').click()

    def test_34_click_discount_cards(self):  # "Проверка кликабельности кнопки 'Дисконтные карты'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_discount_cards()
        self.driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/ul/li[1]/a').click()

    def test_35_click_my_finance(self):  # "Проверка кликабельности кнопки 'Мои финансы
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_my_finance()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/ul/li[6]/a').click()

    def test_36_click_my_digital_library(self):  # "Проверка кликабельности 'Моя электронная библиотека'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_my_digital_library()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/ul/li[7]/a').click()

    def test_37_click_subscription(self):  # "Проверка кликабельности 'Подписка'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_subscription()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/ul/li[9]/a').click()

    def test_38_click_change_password(self):  # "Проверка кликабельности 'Сменить пароль'"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_change_password()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/ul/li[11]/a').click()

    def test_39_new_password_field(self):  # "Наличие поля для ввода нового пароля"
        driver = self.driver
        time.sleep(5)
        #driver.find_element(By.CLASS_NAME, 'amount-form__control amount-form__control_inc js-amount-control').click()
        #driver.find_element(By.NAME, 'action_minus').click()
        driver.find_element(By.XPATH, '//*[@id="name"]').click()

    def test_40_click_link_vk(self):  # "Проверка корректности кнопки с ссылкой на группу в ВК"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_link_vk()
        driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div/div[3]/div/div[1]/div/a[1]').click()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_41_click_link_twitter(self):  # "Проверка корректности кнопки с ссылкой на группу в твиттер"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_link_twitter()
        driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div/div[3]/div/div[1]/div/a[2]').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_42_click_link_youtube(self):  # "Проверка корректности кнопки с ссылкой на группу в ютуб"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_link_youtube()
        driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div/div[3]/div/div[1]/div/a[3]').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_43_click_link_telegram_bot(self):  # "Проверка корректности кнопки с ссылкой на бота в вотсап"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_link_telegram_bot()
        driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div/div[3]/div/div[1]/div/a[4]').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_44_click_link_ok(self):  # "Проверка корректности кнопки с ссылкой на группу в OK"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_link_ok()
        driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div/div[3]/div/div[1]/div/a[4]').click()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_45_click_link_yandex_zen(self):  # "Проверка корректности кнопки с ссылкой на 'Яндекс дзен"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_link_yandex_zen()
        driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div/div[3]/div/div[1]/div/a[6]').click()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_46_catalog_products(self):  # "Проверка выпадающего списка при наведении на каталог товаров"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.catalog_products()
        time.sleep(5)
        driver.find_elements(By.XPATH, '//*[@id="top"]/section[1]/div[1]/ul[1]/li[1]/a')

    def test_47_click_telephone_number(self):  # "Проверка кликабельности кнопки 'Телефонный номер?"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_telephone_number()
        driver.find_element(By.CLASS_NAME, 'header__main__phones__phone').click()

    def test_48_click_email_adress(self):  # "Проверка кликабельности кнопки 'Электронная почта"
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_email_adress()
        driver.find_element(By.CLASS_NAME, 'header__main__phones__mail').click()

    def test_49_lens_product_and_prices(self):  # "Сравнение количества товаров и цен к ним (кат. 'Детская литература')"
        driver = self.driver
        products = driver.find_elements(By.CLASS_NAME, 'book-preview__title-link')
        prices = driver.find_elements(By.CLASS_NAME, 'book-preview__price')
        self.assertEqual(len(products), len(prices))

    def test_50_lens_products_and_imgs(self):  #  "Сравнения количества товаров и картинок к ним "
        driver = self.driver
        products = driver.find_elements(By.CLASS_NAME, 'book-preview__title-link')
        imgs = driver.find_elements(By.CLASS_NAME, 'book-preview__img')
        self.assertEqual(len(products), len(imgs))

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print('Test completed')


if __name__ == '__main__':
    unittest.main()