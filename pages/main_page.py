from .base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    """Класс для работы с главной страницей (конструктор бургеров)."""
    
    def click_personal_account_button(self):
        """Кликнуть на кнопку 'Личный Кабинет'."""
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    def click_constructor_button(self):
        """Кликнуть на кнопку 'Конструктор'."""
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    def click_order_feed_button(self):
        """Кликнуть на кнопку 'Лента заказов'."""
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
    
    def click_login_button(self):
        """Кликнуть на кнопку 'Войти в аккаунт'."""
        self.click_element(MainPageLocators.LOGIN_BUTTON)
    
    def is_constructor_button_visible(self):
        """Проверить, видна ли кнопка 'Конструктор'."""
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_BUTTON)