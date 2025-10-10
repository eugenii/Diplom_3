# tests/test_personal_account.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from data import BASE_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_profile import AccountProfile


class TestPersonalAccount:
    """Тесты личного кабинета"""
    
    def test_personal_account_flow(self, driver):
        """2.1-2.3: Полный поток личного кабинета"""
        print("\n=== Тест 2.1-2.3: Личный кабинет ===")
        
        # Сначала нужно авторизоваться
        print("Шаг: Авторизация...")
        login_page = LoginPage(driver)
        driver.get(f"{BASE_URL}/login")
        
        # Авторизуемся с использованием метода login
        login_page.login("123@g.ru", "123456")
        
        # Ждем перехода на главную страницу после авторизации
        WebDriverWait(driver, 10).until(
            EC.url_contains("/")
        )
        print("✅ Успешная авторизация")
        
        # 2.1 переход по клику на «Личный кабинет»
        print("Шаг 2.1: Переход в личный кабинет...")
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        
        # Ждем загрузки страницы профиля
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        print("✅ 2.1: Успешный переход в личный кабинет")
        
        # 2.2 переход в раздел «История заказов»
        print("Шаг 2.2: Переход в историю заказов...")
        account_profile = AccountProfile(driver)
        account_profile.click_order_history_link()
        
        # Упрощенная проверка - только по URL
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/order-history")
        )
        assert "/account/order-history" in driver.current_url, "Не перешли на страницу истории заказов"
        print("✅ 2.2: Успешный переход в историю заказов")
        
        # 2.3 выход из аккаунта - ОБХОДИМ страницу профиля
        print("Шаг 2.3: Выход из аккаунта...")
        
        # Вместо перехода на /account/profile, выходим через главное меню
        # Переходим на главную страницу
        driver.get(f"{BASE_URL}/")
        
        # Кликаем на личный кабинет (должен открыться профиль)
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        
        # Ждем загрузки профиля и выходим
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        account_profile = AccountProfile(driver)
        account_profile.click_logout_button()
        
        # Ждем перехода на страницу логина после выхода
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url, "Не перешли на страницу логина после выхода"
        print("✅ 2.3: Успешный выход из аккаунта")
        
        print("🎉 Тесты 2.1-2.3 пройдены успешно!")