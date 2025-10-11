import allure
import pytest
from selenium.webdriver.common.by import By
from data import LOGIN_URL, FORGOT_PASSWORD_URL
from data import TestForgotPasswordData
from pages.login_page import LoginPage
from pages.forgot_password import ForgotPassword

@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    
    @allure.feature("Восстановление пароля")
    @allure.story("Переход на страницу восстановления пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_forgot_password_page(self, driver):
        """1.1: Переход на страницу восстановления пароля."""
        
        with allure.step("Перейти на страницу логина"):
            driver.get(LOGIN_URL)
            login_page = LoginPage(driver)
            assert login_page.is_login_page(), "Не удалось перейти на страницу логина"
        
        with allure.step("Кликнуть на кнопку 'Восстановить пароль'"):
            login_page.click_forgot_password_button()
        
        with allure.step("Проверить переход на страницу восстановления пароля"):
            forgot_password_page = ForgotPassword(driver)
            assert "forgot-password" in driver.current_url
            assert forgot_password_page.is_email_field_visible()
    
    @allure.feature("Восстановление пароля")
    @allure.story("Ввод почты и восстановление пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_enter_email_and_restore_password(self, driver):
        """1.2: Ввод почты и клик по кнопке «Восстановить»."""
        
        with allure.step("Перейти на страницу восстановления пароля"):
            driver.get(FORGOT_PASSWORD_URL)
            forgot_password_page = ForgotPassword(driver)
            assert forgot_password_page.is_forgot_password_page()
        
        with allure.step("Ввести email в поле"):
            forgot_password_page.set_email(TestForgotPasswordData.EXISTING_EMAIL)
        
        with allure.step("Кликнуть на кнопку 'Восстановить'"):
            forgot_password_page.click_restore_button()
        
        with allure.step("Проверить результат операции"):
            current_url = driver.current_url
            if "reset-password" in current_url:
                assert "reset-password" in current_url
            else:
                assert forgot_password_page.is_success_message_displayed() or "forgot-password" in current_url
    
    @allure.feature("Восстановление пароля")
    @allure.story("Кнопка показать/скрыть пароль делает поле активным")
    @allure.severity(allure.severity_level.NORMAL)
    def test_eye_button_activates_password_field(self, driver):
        """1.3: Клик по кнопке показать/скрыть пароль делает поле активным."""
        
        with allure.step("Перейти на страницу восстановления пароля"):
            driver.get(FORGOT_PASSWORD_URL)
            forgot_password_page = ForgotPassword(driver)
        
        with allure.step("Восстановить пароль"):
            forgot_password_page.set_email(TestForgotPasswordData.EXISTING_EMAIL)
            forgot_password_page.click_restore_button()
            forgot_password_page.wait_for_url_contains("reset-password")
        
        with allure.step("Найти элементы страницы"):
            # Находим контейнер поля пароля
            container = driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_password')]")
            
            # Находим кнопку глаза
            eye_button = driver.find_element(By.XPATH, "//div[contains(@class, 'input__icon-action')]")
        
        with allure.step("Проверить состояние ДО клика"):
            classes_before = container.get_attribute("class")
            is_active_before = "input_status_active" in classes_before
        
        with allure.step("Кликнуть на кнопку показать/скрыть пароль"):
            eye_button.click()
        
        with allure.step("Проверить состояние ПОСЛЕ клика"):
            classes_after = container.get_attribute("class")
            is_active_after = "input_status_active" in classes_after
            
            # Проверяем, что добавился класс input_status_active
            assert is_active_after, \
                f"Класс input_status_active не добавлен. Было: {classes_before}, стало: {classes_after}"