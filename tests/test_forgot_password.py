import allure
import pytest

from data import TestForgotPasswordData
from pages.login_page import LoginPage
from pages.forgot_password import ForgotPassword

@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    
    @allure.title("1.1: Переход на страницу восстановления пароля")
    def test_go_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPassword(driver)
        
        # Переходим на страницу логина через метод страницы
        login_page.navigate_to_login()
        
        # Переходим на страницу логина через метод страницы
        login_page.click_forgot_password_button()
        
        # Проверяем через методы страниц
        assert forgot_password_page.is_on_forgot_password_page()
        assert forgot_password_page.is_email_field_visible()
    
    @allure.title("1.2: Ввод почты и восстановление пароля")
    def test_enter_email_and_restore_password(self, driver):
        forgot_password_page = ForgotPassword(driver)
        
        # Переходим на страницу восстановления пароля через метод страницы
        forgot_password_page.navigate_to_forgot_password()
        
        forgot_password_page.set_email(TestForgotPasswordData.EXISTING_EMAIL)
        
        # Кликаем через метод страницы (браузер определяется внутри)
        forgot_password_page.click_restore_button()
        
        # Ждем перехода на страницу сброса пароля через метод страницы
        forgot_password_page.wait_for_reset_password_page(10)
        
        # Проверяем через методы страниц
        assert forgot_password_page.is_on_reset_password_page() or forgot_password_page.is_reset_password_page()
    

    @allure.title("1.3: Кнопка показать/скрыть пароль делает поле активным")
    def test_eye_button_activates_password_field(self, driver):
        """Тест проверяет, что кнопка глаза меняет класс контейнера и тип поля."""
        forgot_password_page = ForgotPassword(driver)
        
        # Переходим на страницу восстановления пароля через метод страницы
        forgot_password_page.navigate_to_forgot_password()
        
        forgot_password_page.set_email(TestForgotPasswordData.EXISTING_EMAIL)
        
        # Кликаем через метод страницы (браузер определяется внутри)
        forgot_password_page.click_restore_button()
        
        # Ждем перехода на страницу сброса пароля через метод страницы
        forgot_password_page.wait_for_reset_password_page(10)
        
        # Проверяем состояние ДО клика
        type_before = forgot_password_page.get_password_field_type()
        container_before = forgot_password_page.get_password_container_classes()
        print(f"ДО клика - Тип: {type_before}, Контейнер: {container_before}")
        
        # Убеждаемся, что начальное состояние правильное
        assert type_before == "password", f"Тип поля должен быть 'password', но: {type_before}"
        assert "input_type_password" in container_before, f"Контейнер должен содержать input_type_password, но: {container_before}"
        
        # Кликаем на кнопку глаза
        forgot_password_page.click_show_hide_password_button()
        
        # Ждем изменения состояния с явными ожиданиями (вместо time.sleep)
        forgot_password_page.wait_for_password_field_change(timeout=5)
        forgot_password_page.wait_for_container_change(timeout=5)
        
        # Проверяем состояние ПОСЛЕ клика
        type_after = forgot_password_page.get_password_field_type()
        container_after = forgot_password_page.get_password_container_classes()
        print(f"ПОСЛЕ клика - Тип: {type_after}, Контейнер: {container_after}")
        
        # Основные проверки после клика:
        # 1. Тип поля должен измениться на text
        assert type_after == "text", f"Тип поля должен быть 'text' после клика, но: {type_after}"
        
        # 2. Контейнер должен содержать input_type_text
        assert "input_type_text" in container_after, f"Контейнер должен содержать input_type_text после клика, но: {container_after}"
        
        # 3. Контейнер не должен содержать input_type_password
        assert "input_type_password" not in container_after, f"Контейнер не должен содержать input_type_password после клика, но: {container_after}"
        
        # 4. Дополнительно: должен появиться класс input_status_active
        assert "input_status_active" in container_after, f"Контейнер должен содержать input_status_active после клика, но: {container_after}"
        
        print("✅ Тест пройден: кнопка глаза успешно меняет тип поля и классы контейнера")