from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators

class ForgotPassword(BasePage):
    """Класс для работы со страницей восстановления пароля."""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordLocators()  # ✅ Добавляем локаторы
        
    def set_email(self, email):
        """Ввести email в поле."""
        self.input_text(ForgotPasswordLocators.EMAIL_INPUT, email)
    
    def click_restore_button(self):
        """Кликнуть на кнопку 'Восстановить'."""
        self.click_element(ForgotPasswordLocators.RESTORE_BUTTON)