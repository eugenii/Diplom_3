from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    """Класс для работы со страницей логина."""
    def click_forgot_password_link(self):
        """Кликнуть на ссылку 'Восстановить пароль'."""
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)