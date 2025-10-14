# [file name]: pages/constructor_page.py
from .base_page import BasePage
from locators.constructor_locators import ConstructorLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConstructorPage(BasePage):
    """Класс для работы с конструктором бургеров."""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Получить значение каунтера ингредиента")
    def get_ingredient_counter_value(self, ingredient_locator):
        """Получить значение каунтера для конкретного ингредиента."""
        try:
            # Находим ингредиент
            ingredient = self.find_element(ingredient_locator)
            # Ищем каунтер внутри ингредиента
            counter = ingredient.find_element(*ConstructorLocators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text else 0
        except:
            return 0
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self, ingredient_locator):
        """Перетащить ингредиент в зону конструктора."""
        # Ждем пока ингредиент станет доступным
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ingredient_locator)
        )
        
        # Перетаскиваем
        self.drag_and_drop(ingredient_locator, ConstructorLocators.CONSTRUCTOR_DROP_ZONE)
        
        # Ждем обновления каунтера
        WebDriverWait(self.driver, 5).until(
            lambda d: self.get_ingredient_counter_value(ingredient_locator) > 0
        )
    
    @allure.step("Добавить булку в конструктор")
    def add_bun_to_constructor(self):
        """Добавить булку в конструктор."""
        initial_counter = self.get_bun_counter()
        self.drag_ingredient_to_constructor(ConstructorLocators.BUN_INGREDIENT)
        return self.get_bun_counter() > initial_counter
    
    @allure.step("Добавить соус в конструктор")
    def add_sauce_to_constructor(self):
        """Добавить соус в конструктор."""
        initial_counter = self.get_sauce_counter()
        self.drag_ingredient_to_constructor(ConstructorLocators.SAUCE_INGREDIENT)
        return self.get_sauce_counter() > initial_counter
    
    @allure.step("Добавить начинку в конструктор")
    def add_filling_to_constructor(self):
        """Добавить начинку в конструктор."""
        initial_counter = self.get_filling_counter()
        self.drag_ingredient_to_constructor(ConstructorLocators.FILLING_INGREDIENT)
        return self.get_filling_counter() > initial_counter
    
    @allure.step("Получить каунтер булки")
    def get_bun_counter(self):
        return self.get_ingredient_counter_value(ConstructorLocators.BUN_INGREDIENT)
    
    @allure.step("Получить каунтер соуса")
    def get_sauce_counter(self):
        return self.get_ingredient_counter_value(ConstructorLocators.SAUCE_INGREDIENT)
    
    @allure.step("Получить каунтер начинки")
    def get_filling_counter(self):
        return self.get_ingredient_counter_value(ConstructorLocators.FILLING_INGREDIENT)