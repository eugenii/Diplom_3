from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    """Класс для работы с главной страницей и навигацией."""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor_button(self):
        """Кликнуть на кнопку конструктора в хедере."""
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Кликнуть на 'Лента Заказов'")
    def click_order_feed_button(self):
        """Кликнуть на кнопку ленты заказов в хедере."""
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Проверить, что открыт конструктор")
    def is_constructor_opened(self):
        """Проверить, что открыта страница конструктора."""
        constructor_visible = self.is_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)
        ingredients_visible = self.is_element_visible(MainPageLocators.INGREDIENTS_SECTION)
        burger_constructor_visible = self.is_element_visible(MainPageLocators.BURGER_CONSTRUCTOR)
        
        return constructor_visible and ingredients_visible and burger_constructor_visible
    
    @allure.step("Проверить, что открыта лента заказов")
    def is_order_feed_opened(self):
        """Проверить, что открыта страница ленты заказов."""
        return self.is_element_visible(MainPageLocators.ORDER_FEED_TITLE)
    
    @allure.step("Кликнуть на раздел 'Булки'")
    def click_buns_section(self):
        """Кликнуть на раздел булок в конструкторе."""
        self.click_element(MainPageLocators.BUNS_SECTION)
    
    @allure.step("Кликнуть на раздел 'Соусы'")
    def click_sauces_section(self):
        """Кликнуть на раздел соусов в конструкторе."""
        self.click_element(MainPageLocators.SAUCES_SECTION)
    
    @allure.step("Кликнуть на раздел 'Начинки'")
    def click_fillings_section(self):
        """Кликнуть на раздел начинок в конструкторе."""
        self.click_element(MainPageLocators.FILLINGS_SECTION)
    
    @allure.step("Получить активный раздел конструктора")
    def get_active_section(self):
        """Получить текст активного раздела конструктора."""
        try:
            active_section = self.find_element(MainPageLocators.ACTIVE_SECTION)
            return active_section.text
        except:
            return ""
    
    @allure.step("Перейти на главную страницу")
    def go_to_main_page(self):
        """Перейти на главную страницу."""
        self.driver.get(self.base_url)