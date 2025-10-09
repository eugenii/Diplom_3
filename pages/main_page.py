# pages/main_page.py (должно быть так)
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    """Класс для работы с главной страницей (конструктор бургеров)."""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()  # ✅ Важно!
    
    def click_constructor_button(self):
        """Кликнуть на кнопку 'Конструктор'."""
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)
    
    def click_order_feed_button(self):
        """Кликнуть на кнопку 'Лента заказов'."""
        self.click_element(self.locators.ORDER_FEED_BUTTON)

    # Новые методы для работы с ингредиентами
    def click_first_ingredient(self):
        """Кликнуть на первый ингредиент в списке."""
        self.click_element(self.locators.FIRST_INGREDIENT)
    
    def is_modal_visible(self):
        """Проверить, видно ли модальное окно."""
        return self.is_element_visible(self.locators.MODAL_TITLE)
    
    def close_modal(self):
        """Закрыть модальное окно кликом на крестик."""
        self.click_element(self.locators.MODAL_CLOSE_BUTTON)
    
    def is_modal_closed(self):
        """Проверить, закрыто ли модальное окно."""
        return not self.is_element_visible(self.locators.MODAL_OVERLAY)