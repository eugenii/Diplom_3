import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators

class ForgotPassword(BasePage):
    """Класс для работы со страницей восстановления пароля."""
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Перейти на страницу восстановления пароля")
    def navigate_to_forgot_password(self):
        self.navigate_to("https://stellarburgers.education-services.ru/forgot-password")
    
    @allure.step("Ввести email")
    def set_email(self, email):
        self.input_text(ForgotPasswordLocators.EMAIL_INPUT, email)
    
    @allure.step("Кликнуть 'Восстановить'")
    def click_restore_button(self, browser_name="chrome"):
        self.safe_click_with_modal_check(ForgotPasswordLocators.RESTORE_BUTTON, browser_name)
    
    @allure.step("Проверить видимость поля email")
    def is_email_field_visible(self):
        return self.is_element_visible(ForgotPasswordLocators.EMAIL_INPUT)
    
    @allure.step("Проверить страницу восстановления")
    def is_forgot_password_page(self):
        return self.is_element_visible(ForgotPasswordLocators.FORGOT_PASSWORD_HEADER)
    
    @allure.step("Проверить переход на страницу сброса пароля")
    def is_reset_password_page(self):
        return self.is_element_visible(ForgotPasswordLocators.RESET_PASSWORD_HEADER)
    
    @allure.step("Кликнуть на кнопку показать/скрыть пароль")
    def click_show_hide_password_button(self):
        self.click_element(ForgotPasswordLocators.EYE_BUTTON)
    
    @allure.step("Дождаться изменения типа поля пароля")
    def wait_for_password_field_change(self, timeout=10):
        """Дождаться, когда тип поля изменится с password на text."""
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_password_field_type() == "text"
        )
    
    @allure.step("Дождаться изменения класса контейнера")
    def wait_for_container_change(self, timeout=10):
        """Дождаться, когда контейнер получит класс input_type_text."""
        WebDriverWait(self.driver, timeout).until(
            lambda d: "input_type_text" in self.get_password_container_classes()
        )
    
    @allure.step("Проверить видимость поля пароля")
    def is_password_field_visible(self):
        """Проверить видимость поля пароля."""
        return self.is_element_visible(ForgotPasswordLocators.PASSWORD_INPUT)
    
    @allure.step("Проверить видимость кнопки глаза")
    def is_eye_button_visible(self):
        """Проверить видимость кнопки глаза."""
        return self.is_element_visible(ForgotPasswordLocators.EYE_BUTTON)
    
    @allure.step("Проверить, что поле пароля активно")
    def is_password_field_active(self):
        """Проверить, что поле пароля стало видимым после клика на глаз."""
        try:
            container_classes = self.get_password_container_classes()
            return "input_type_text" in container_classes and "input_status_active" in container_classes
        except Exception as e:
            return False
    
    @allure.step("Получить тип поля пароля")
    def get_password_field_type(self):
        """Получить текущий тип поля пароля."""
        try:
            password_field = self.find_element(ForgotPasswordLocators.PASSWORD_INPUT)
            return password_field.get_attribute("type")
        except:
            return "unknown"
    
    @allure.step("Получить классы контейнера пароля")
    def get_password_container_classes(self):
        """Получить классы контейнера поля пароля."""
        try:
            password_container = self.find_element(ForgotPasswordLocators.PASSWORD_CONTAINER)
            return password_container.get_attribute("class")
        except:
            return "unknown"