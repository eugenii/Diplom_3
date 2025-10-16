from .base_page import BasePage
from locators.login_locators import LoginLocators
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Ввести email")
    def set_email(self, email):
        self.input_text(LoginLocators.EMAIL_INPUT, email)
    
    @allure.step("Ввести пароль")
    def set_password(self, password):
        self.input_text(LoginLocators.PASSWORD_INPUT, password)
    
    @allure.step("Кликнуть кнопку Войти")
    def click_login_button(self):
        self.click_element(LoginLocators.LOGIN_BUTTON)
    
    @allure.step("Кликнуть 'Восстановить пароль'")
    def click_forgot_password_button(self, browser_name="chrome"):
        self.safe_click_with_modal_check(LoginLocators.FORGOT_PASSWORD_BUTTON, browser_name)