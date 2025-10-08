from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    """Класс для работы со страницей логина."""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()  # ✅ Добавляем локаторы
    def click_forgot_password_link(self):
        """Кликнуть на ссылку 'Восстановить пароль'."""
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def click_show_hide_password(self):
        """Кликнуть на кнопку показать/скрыть пароль."""
        self.click_element(self.locators.SHOW_HIDE_PASSWORD_BUTTON)

    # def is_password_visible(self):
    #     """Проверяет, отображается ли пароль текстом."""
    #     password_field = self.find_element(self.locators.PASSWORD_INPUT)
    #     return password_field.get_attribute("type") == "text"
    
    def is_password_visible(self):
        """Проверяет, отображается ли пароль текстом (вместо звездочек)."""
        password_field = self.find_element(self.locators.PASSWORD_INPUT)
        field_type = password_field.get_attribute("type")
        return field_type == "text"  # Если type="text" - пароль виден
    
    # pages/login_page.py (дополняем)
    def login(self, email, password):
        """Выполнить авторизацию."""
        self.input_text(self.locators.EMAIL_INPUT, email)
        self.input_text(self.locators.PASSWORD_INPUT, password)
        self.click_element(self.locators.LOGIN_BUTTON)
