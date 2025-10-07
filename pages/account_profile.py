from .base_page import BasePage
from locators.account_profile_locators import AccountProfileLocators

class AccountProfile(BasePage):
    """Класс для работы со страницей профиля в личном кабинете."""
    
    def click_logout_button(self):
        """Кликнуть на кнопку 'Выход'."""
        self.click_element(AccountProfileLocators.LOGOUT_BUTTON)
    
    def is_profile_page_loaded(self):
        """Проверить, что страница профиля загружена."""
        return self.is_element_visible(AccountProfileLocators.PROFILE_HEADER)