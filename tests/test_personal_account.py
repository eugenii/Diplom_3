import allure
import pytest
from data import LOGIN_URL, PERSONAL_ACCOUNT_URL
from data import TestUser
from pages.login_page import LoginPage
from pages.personal_account import PersonalAccount

@pytest.mark.usefixtures("driver")
class TestPersonalAccount:
    """Тесты для личного кабинета."""
    
    @allure.feature("Личный кабинет")
    @allure.story("Переход по клику на «Личный кабинет»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_personal_account(self, driver):
        """2.1: Переход по клику на «Личный кабинет»."""
        # TODO: Реализовать после продолжения
        pass
    
    @allure.feature("Личный кабинет")
    @allure.story("Переход в раздел «История заказов»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_order_history(self, driver):
        """2.2: Переход в раздел «История заказов»."""
        # TODO: Реализовать после продолжения
        pass
    
    @allure.feature("Личный кабинет")
    @allure.story("Выход из аккаунта")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_from_account(self, driver):
        """2.3: Выход из аккаунта."""
        # TODO: Реализовать после продолжения
        pass