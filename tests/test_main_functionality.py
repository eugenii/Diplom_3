# [file name]: tests/test_main_functionality_simple.py
# [file content begin]
import allure
import pytest
from data import BASE_URL, LOGIN_URL
from data import TestUser
from pages.main_page import MainPage
from pages.personal_account import PersonalAccount
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestMainFunctionalitySimple:
    """Упрощенные тесты для основного функционала - только 2 основных теста."""
    
    def _login_user(self, driver):
        """Вспомогательный метод для авторизации пользователя."""
        login_page = LoginPage(driver)
        driver.get(LOGIN_URL)
        login_page.set_email(TestUser.EMAIL)
        login_page.set_password(TestUser.PASSWORD)
        login_page.click_login_button()
        return MainPage(driver)
    
    @allure.feature("Основной функционал")
    @allure.story("Переход по клику на «Конструктор»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_constructor(self, driver):
        """3.1: Переход по клику на «Конструктор»."""
        
        with allure.step("Авторизовать пользователя и перейти в личный кабинет"):
            main_page = self._login_user(driver)
            personal_account = PersonalAccount(driver)
            personal_account.click_personal_account_button()
            assert "account" in driver.current_url, "Не удалось перейти в личный кабинет"
        
        with allure.step("Кликнуть на 'Конструктор' в хедере"):
            main_page.click_constructor_button()
        
        with allure.step("Проверить переход в конструктор"):
            assert main_page.is_constructor_opened(), "Не удалось перейти в конструктор"
            assert BASE_URL in driver.current_url, "URL не соответствует конструктору"
    
    @allure.feature("Основной функционал")
    @allure.story("Переход по клику на «Лента заказов»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_order_feed(self, driver):
        """3.2: Переход по клику на «Лента заказов»."""
        
        with allure.step("Перейти на главную страницу"):
            main_page = MainPage(driver)
            driver.get(BASE_URL)  # Используем прямой переход вместо go_to_main_page
            assert main_page.is_constructor_opened(), "Не открылся конструктор на главной"
        
        with allure.step("Кликнуть на 'Лента Заказов' в хедере"):
            main_page.click_order_feed_button()
        
        with allure.step("Проверить переход в ленту заказов"):
            assert main_page.is_order_feed_opened(), "Не удалось перейти в ленту заказов"
            assert "feed" in driver.current_url, "URL не соответствует ленте заказов"
# [file content end]