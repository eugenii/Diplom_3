import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_profile import AccountProfile
from data import TestUser

class TestPersonalAccount:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.account_profile = AccountProfile(driver)

    def login_user(self):
        """Вспомогательный метод для логина пользователя"""
        # Переходим на страницу логина
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        
        # Логинимся (пока используем заглушку)
        # TODO: Реализовать реальный логин когда настроим данные пользователя
        print("Логиним пользователя...")

    @allure.title('Переход в личный кабинет по клику')
    def test_go_to_personal_account(self):
        """Тест 2.1: Переход по клику на «Личный кабинет»"""
        # Переходим на главную страницу
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Кликаем на кнопку "Личный кабинет"
        self.main_page.click_personal_account_button()
        
        # Проверяем, что перешли на страницу логина (т.к. не авторизованы)
        assert "/login" in self.driver.current_url
        print("✅ Успешно перешли на страницу логина при клике на Личный кабинет")

    @allure.title('Выход из аккаунта')
    @pytest.mark.skip(reason="Требуется реализация логина пользователя")
    def test_logout_from_account(self):
        """Тест 2.3: Выход из аккаунта"""
        # TODO: Реализовать после настройки логина
        # 1. Залогиниться
        # 2. Перейти в личный кабинет
        # 3. Нажать кнопку "Выход"
        # 4. Проверить, что вышли из аккаунта
        pytest.skip("Требуется реализация логина пользователя")

    @allure.title('Переход в раздел История заказов')
    @pytest.mark.skip(reason="Требуется реализация перехода в историю заказов")
    def test_go_to_order_history(self):
        """Тест 2.2: Переход в раздел «История заказов»"""
        # TODO: Реализовать после настройки основных переходов
        pytest.skip("Требуется реализация перехода в историю заказов")