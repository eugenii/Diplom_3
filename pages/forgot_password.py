from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
import allure

class ForgotPassword(BasePage):
    """Класс для работы со страницей восстановления пароля."""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Ввести email")
    def set_email(self, email):
        self.input_text(ForgotPasswordLocators.EMAIL_INPUT, email)
    
    @allure.step("Кликнуть 'Восстановить'")
    def click_restore_button(self):
        self.click_element(ForgotPasswordLocators.RESTORE_BUTTON)
    
    @allure.step("Проверить видимость поля email")
    def is_email_field_visible(self):
        return self.is_element_visible(ForgotPasswordLocators.EMAIL_INPUT)
    
    @allure.step("Проверить страницу восстановления")
    def is_forgot_password_page(self):
        return self.is_element_visible(ForgotPasswordLocators.FORGOT_PASSWORD_HEADER)
    
    @allure.step("Проверить сообщение об успехе")
    def is_success_message_displayed(self):
        return self.is_element_visible(ForgotPasswordLocators.SUCCESS_MESSAGE)
    
    @allure.step("Кликнуть на кнопку показать/скрыть пароль")
    def click_show_hide_password_button(self):
        self.click_element(ForgotPasswordLocators.EYE_BUTTON)
    
    @allure.step("Проверить, что поле пароля активно")
    def is_password_field_active(self):
        """Проверить наличие класса input_status_active у контейнера поля."""
        try:
            container = self.find_element(ForgotPasswordLocators.PASSWORD_CONTAINER)
            classes = container.get_attribute("class")
            return "input_status_active" in classes
        except:
            return False
    
    @allure.step("Проверить видимость поля пароля")
    def is_password_field_visible(self):
        return self.is_element_visible(ForgotPasswordLocators.PASSWORD_FIELD)
    
    @allure.step("Проверить видимость кнопки глаза")
    def is_eye_button_visible(self):
        return self.is_element_visible(ForgotPasswordLocators.EYE_BUTTON)