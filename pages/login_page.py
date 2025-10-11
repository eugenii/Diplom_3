from .base_page import BasePage
from locators.login_locators import LoginLocators
import allure

class LoginPage(BasePage):
    """Класс для работы со страницей логина."""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Кликнуть на кнопку 'Восстановить пароль'")
    def click_forgot_password_button(self):
        """Кликнуть на кнопку восстановления пароля."""
        self.click_element(LoginLocators.FORGOT_PASSWORD_BUTTON)
    
    @allure.step("Проверить, что находимся на странице логина")
    def is_login_page(self):
        """Проверить, что открыта страница логина."""
        return self.is_element_visible(LoginLocators.LOGIN_HEADER)
    
    @allure.step("Ввести email: {email}")
    def set_email(self, email):
        """Ввести email."""
        self.input_text(LoginLocators.EMAIL_INPUT, email)
    
    @allure.step("Ввести пароль")
    def set_password(self, password):
        """Ввести пароль."""
        self.input_text(LoginLocators.PASSWORD_INPUT, password)
    
    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_login_button(self):
        """Кликнуть на кнопку входа."""
        self.click_element(LoginLocators.LOGIN_BUTTON)