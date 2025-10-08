# pages/account_profile.py (дополняем)
from .base_page import BasePage
from locators.account_profile_locators import AccountProfileLocators

class AccountProfile(BasePage):
    """Класс для работы со страницей профиля в личном кабинете."""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AccountProfileLocators()
    
    def click_logout_button(self):
        """Кликнуть на кнопку 'Выход'."""
        self.click_element(self.locators.LOGOUT_BUTTON)
    
    def click_order_history_link(self):
        """Кликнуть на ссылку 'История заказов'."""
        self.click_element(self.locators.ORDER_HISTORY_LINK)
    
    def is_profile_page_loaded(self):
        """Проверить, что страница профиля загружена."""
        return self.is_element_visible(self.locators.PROFILE_HEADER)