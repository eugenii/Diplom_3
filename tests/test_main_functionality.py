import allure
import pytest

from data import BASE_URL, LOGIN_URL
from data import TestUser
from pages.main_page import MainPage
from pages.personal_account import PersonalAccount
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestMainFunctionality:
    
    def _login_user(self, driver):
        login_page = LoginPage(driver)
        driver.get(LOGIN_URL)
        login_page.set_email(TestUser.EMAIL)
        login_page.set_password(TestUser.PASSWORD)
        login_page.click_login_button()
        return MainPage(driver)
    
    @allure.title("3.1: Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        main_page = self._login_user(driver)
        personal_account = PersonalAccount(driver)
        
        personal_account.click_personal_account_button()
        main_page.click_constructor_button()
        
        assert main_page.is_constructor_opened()
        assert BASE_URL in driver.current_url
    
    @allure.title("3.2: Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        driver.get(BASE_URL)
        
        main_page.click_order_feed_button()
        
        assert main_page.is_order_feed_opened()
        assert "feed" in driver.current_url