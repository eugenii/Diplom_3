# tests/test_forgot_password.py
import pytest

from data import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.forgot_password import ForgotPassword


class TestForgotPassword:
    """Тесты восстановления пароля"""
    
    def test_restore_password_flow(self, driver):
        """1.1-1.2: Полный поток восстановления пароля"""
        print("\n=== Тест 1.1-1.2: Восстановление пароля ===")
        
        # 1.1 Переход на страницу восстановления пароля по кнопке «Восстановить пароль»
        print("Шаг 1.1: Переход на страницу восстановления пароля...")
        login_page = LoginPage(driver)
        driver.get(f"{BASE_URL}/login")
        
        # Проверяем, что находимся на странице логина
        assert "/login" in driver.current_url, "Не находимся на странице логина"
        print("✅ Находимся на странице логина")
        
        # Кликаем на ссылку "Восстановить пароль"
        login_page.click_forgot_password_link()
        
        # Ждем перехода на страницу восстановления
        WebDriverWait(driver, 10).until(
            EC.url_contains("/forgot-password")
        )
        assert "/forgot-password" in driver.current_url, "Не перешли на страницу восстановления пароля"
        print("✅ 1.1: Успешный переход на страницу восстановления пароля")
        
        # 1.2 Ввод почты и клик по кнопке «Восстановить»
        print("Шаг 1.2: Ввод email и восстановление...")
        forgot_password_page = ForgotPassword(driver)
        
        # Проверяем, что элементы присутствуют на странице
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(forgot_password_page.locators.EMAIL_INPUT)
        )
        restore_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(forgot_password_page.locators.RESTORE_BUTTON)
        )
        print("✅ Все элементы присутствуют на странице восстановления")
        
        # Вводим email и кликаем кнопку восстановления
        test_email = "test@example.com"
        forgot_password_page.set_email(test_email)
        print(f"✅ Введен email: {test_email}")
        
        forgot_password_page.click_restore_button()
        print("✅ Нажата кнопка 'Восстановить'")
        
        # Ждем перехода на страницу сброса пароля
        WebDriverWait(driver, 10).until(
            EC.url_contains("/reset-password")
        )
        
        # Проверяем переход на страницу сброса пароля
        assert "/reset-password" in driver.current_url, "Не перешли на страницу сброса пароля"
        print("✅ 1.2: Успешный ввод email и переход на страницу сброса пароля")
        
        print("🎉 Тесты 1.1-1.2 пройдены успешно!")

    def test_password_visibility_toggle(self, driver):
        """1.3: Проверка кнопки показать/скрыть пароль НА СТРАНИЦЕ ЛОГИНА"""
        print("\n=== Тест 1.3: Показать/скрыть пароль на странице логина ===")
        
        # Переходим прямо на страницу ЛОГИНА
        login_page = LoginPage(driver)
        driver.get(f"{BASE_URL}/login")
        
        print("✅ Перешли на страницу логина")
        
        # Находим поле пароля и вводим тестовый текст
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(login_page.locators.PASSWORD_INPUT)
        )
        password_field.send_keys("test123")
        
        # Проверяем исходное состояние (должно быть type="password")
        initial_type = password_field.get_attribute("type")
        print(f"Исходный тип поля: {initial_type}")
        
        # Кликаем на глазик (должен изменить type на "text")
        login_page.click_show_hide_password()
        
        # Проверяем новое состояние
        new_type = password_field.get_attribute("type")
        print(f"Тип поля после клика: {new_type}")
        
        # Проверяем, что тип изменился (функциональность работает)
        assert initial_type != new_type, "Тип поля пароля не изменился после клика"
        print("✅ Тип поля пароля изменился - функциональность работает")
        
        # Дополнительная проверка: если изначально был "password", то стал "text"
        if initial_type == "password":
            assert new_type == "text", "Пароль не стал видимым"
            print("✅ Пароль стал видимым (type='text')")
        else:
            assert new_type == "password", "Пароль не скрылся" 
            print("✅ Пароль скрылся (type='password')")
        
        print("✅ 1.3: Кнопка показать/скрыть пароль делает поле активным")