from .base_page import BasePage
from locators.account_history_locators import AccountHistoryLocators

class AccountHistory(BasePage):
    """Класс для работы со страницей истории заказов."""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AccountHistoryLocators()
    
    def is_history_page_loaded(self):
        """Проверить, что страница истории заказов загружена."""
        return self.is_element_visible(self.locators.HISTORY_HEADER)