# login_page.py - добавляем безопасные клики
import allure

from .base_page import BasePage
from locators.login_locators import LoginLocators


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
        # Используем безопасный клик для Firefox
        browser_name = self.get_browser_name()
        self.safe_click_with_modal_check(LoginLocators.LOGIN_BUTTON, browser_name)
    
    @allure.step("Кликнуть 'Восстановить пароль'")
    def click_forgot_password_button(self):
        browser_name = self.get_browser_name()
        self.safe_click_with_modal_check(LoginLocators.FORGOT_PASSWORD_BUTTON, browser_name)

    @allure.step("Перейти на страницу логина")
    def navigate_to_login(self):
        self.navigate_to("https://stellarburgers.education-services.ru/login")

    @allure.step("Проверить, что находимся на странице логина")
    def is_login_page(self):
        return self.is_url_contains("login")