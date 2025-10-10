# tests/test_main_functionality.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from data import BASE_URL
from pages.main_page import MainPage


class TestMainFunctionality:
    """Тесты основного функционала"""
    
    def test_navigation_constructor_and_feed(self, driver):
        """3.1-3.2: Переходы по клику на Конструктор и Лента заказов"""
        print("\n=== Тест 3.1-3.2: Навигация ===")
        
        # Переходим на главную страницу
        main_page = MainPage(driver)
        driver.get(f"{BASE_URL}/")
        
        print("✅ Перешли на главную страницу")
        
        # 3.2 переход по клику на «Лента заказов»
        print("Шаг 3.2: Переход в ленту заказов...")
        main_page.click_order_feed_button()
        
        # Проверяем переход на ленту заказов
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )
        assert "/feed" in driver.current_url, "Не перешли на ленту заказов"
        print("✅ 3.2: Успешный переход в ленту заказов")
        
        # 3.1 переход по клику на «Конструктор»
        print("Шаг 3.1: Возврат в конструктор...")
        main_page.click_constructor_button()
        
        # Проверяем возврат на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_contains("/")
        )
        assert "/" in driver.current_url, "Не вернулись в конструктор"
        print("✅ 3.1: Успешный возврат в конструктор")
        
        print("🎉 Тесты 3.1-3.2 пройдены успешно!")

    def test_ingredient_modal(self, driver):
        """3.3-3.4: Модальное окно ингредиента и закрытие"""
        print("\n=== Тест 3.3-3.4: Модальное окно ингредиента ===")
        
        # Переходим на главную страницу
        main_page = MainPage(driver)
        driver.get(f"{BASE_URL}/")
        
        print("✅ Перешли на главную страницу")
        
        # 3.3 если кликнуть на ингредиент, появится всплывающее окно с деталями
        print("Шаг 3.3: Клик на ингредиент...")
        main_page.click_first_ingredient()
        
        # Проверяем, что модальное окно открылось
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(main_page.locators.MODAL_TITLE)
        )
        assert main_page.is_modal_visible(), "Модальное окно не открылось"
        print("✅ 3.3: Модальное окно с деталями ингредиента открылось")
        
        # 3.4 всплывающее окно закрывается кликом по крестику
        print("Шаг 3.4: Закрытие модального окна...")
        main_page.close_modal()
        
        # Проверяем, что модальное окно закрылось
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(main_page.locators.MODAL_OVERLAY)
        )
        assert main_page.is_modal_closed(), "Модальное окно не закрылось"
        print("✅ 3.4: Модальное окно закрылось по клику на крестик")
        
        print("🎉 Тесты 3.3-3.4 пройдены успешно!")

    def test_ingredient_counter_increases(self, driver):
        """3.5: При добавлении ингредиента в заказ увеличивается каунтер"""
        print("\n=== Тест 3.5: Каунтер ингредиентов ===")
        
        # Переходим на главную страницу с новым URL
        main_page = MainPage(driver)
        driver.get("https://stellarburgers.education-services.ru/")
        
        print("✅ Перешли на главную страницу")
        
        # Получаем начальное значение каунтера булки
        initial_counter = main_page.get_counter_value(main_page.locators.BUN_COUNTER)
        print(f"Начальное значение каунтера: {initial_counter}")
        
        # Перетаскиваем булку в конструктор
        print("Перетаскиваем булку в конструктор...")
        main_page.drag_and_drop(main_page.locators.BUN_INGREDIENT, main_page.locators.CONSTRUCTOR_AREA)
        
        # Проверяем, что каунтер увеличился
        WebDriverWait(driver, 5).until(
            lambda d: main_page.get_counter_value(main_page.locators.BUN_COUNTER) > initial_counter
        )
        
        final_counter = main_page.get_counter_value(main_page.locators.BUN_COUNTER)
        print(f"Конечное значение каунтера: {final_counter}")
        
        assert final_counter > initial_counter, "Каунтер не увеличился после добавления ингредиента"
        print("✅ 3.5: Каунтер ингредиента увеличился после добавления в заказ")