import allure
import pytest

from data import LOGIN_URL
from data import TestUser
from pages.login_page import LoginPage
from pages.personal_account import PersonalAccount

@pytest.mark.usefixtures("driver")
class TestPersonalAccount:
    
    def _login_user(self, driver):
        login_page = LoginPage(driver)
        driver.get(LOGIN_URL)
        login_page.set_email(TestUser.EMAIL)
        login_page.set_password(TestUser.PASSWORD)
        login_page.click_login_button()
        return PersonalAccount(driver)
    
    @allure.title("2.1: Переход по клику на «Личный кабинет»")
    def test_go_to_personal_account(self, driver):
        personal_account = self._login_user(driver)
        personal_account.click_personal_account_button()
        
        assert "account" in driver.current_url
        assert personal_account.is_profile_page()
    
    @allure.title("2.2: Переход в раздел «История заказов»")
    def test_go_to_order_history(self, driver):
        personal_account = self._login_user(driver)
        personal_account.click_personal_account_button()
        personal_account.click_order_history_section()
        
        assert personal_account.is_order_history_page()
    
    @allure.title("2.3: Выход из аккаунта")
    def test_logout_from_account(self, driver):
        personal_account = self._login_user(driver)
        personal_account.click_personal_account_button()
        personal_account.click_logout_button()
        
        assert personal_account.is_logout_successful()
        assert "login" in driver.current_url