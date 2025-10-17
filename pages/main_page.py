import allure

from selenium.webdriver import ActionChains

from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Класс для работы с главной страницей и навигацией."""
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor_button(self):
        """Кликнуть на кнопку конструктора в хедере."""
        return self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON, use_js=True)
    
    @allure.step("Кликнуть на 'Лента Заказов'")
    def click_order_feed_button(self):
        """Кликнуть на кнопку ленты заказов в хедере."""
        return self.click_element(MainPageLocators.ORDER_FEED_BUTTON, use_js=True)
    
    
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
        return self.click_element(MainPageLocators.BUNS_SECTION, use_js=True)
    
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

    @allure.step("Перетащить элемент в конструктор")
    def drag_element_to_constructor(self, element, target_locator):
        """Перетащить элемент в зону конструктора."""
        target = self.find_element(target_locator)
        ActionChains(self.driver).drag_and_drop(element, target).perform()
    
    @allure.step("Добавить булку в конструктор")
    def add_bun_to_constructor(self):
        """Добавить булку в конструктор."""
        bun = self.find_element(MainPageLocators.BUN_INGREDIENT)
        self.drag_element_to_constructor(bun, MainPageLocators.CONSTRUCTOR_AREA)
    
    @allure.step("Добавить соус в конструктор")
    def add_sauce_to_constructor(self):
        """Добавить соус в конструктор."""
        sauce = self.find_element(MainPageLocators.SAUCE_INGREDIENT)
        self.drag_element_to_constructor(sauce, MainPageLocators.CONSTRUCTOR_AREA)

    
    @allure.step("Добавить начинку в конструктор")
    def add_filling_to_constructor(self):
        """Добавить начинку в конструктор."""
        filling = self.find_element(MainPageLocators.FILLING_INGREDIENT)
        constructor_area = self.find_element(MainPageLocators.CONSTRUCTOR_AREA)
        ActionChains(self.driver).drag_and_drop(filling, constructor_area).perform()

    @allure.step("Закрыть модальное окно если есть")
    def close_modal_if_present(self):
        """Закрывает модальное окно если оно есть (для Firefox)"""
        try:
            modal_overlay = self.driver.find_element(By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")
            close_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
            close_button.click()
            return True
        except:
            return False