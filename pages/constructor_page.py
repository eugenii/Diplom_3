from .base_page import BasePage
from locators.constructor_locators import ConstructorLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self, ingredient_locator, browser_name="chrome"):
        # Ждем появления ингредиента
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ingredient_locator)
        )
        
        # Ждем, пока ингредиент станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ingredient_locator)
        )
        
        # Ждем появления области конструктора
        constructor_area = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ConstructorLocators.CONSTRUCTOR_AREA)
        )
        
        if browser_name.lower() == "firefox":
            # Для Firefox используем альтернативный метод перетаскивания
            self._drag_and_drop_firefox(ingredient, constructor_area)
        else:
            # Для Chrome используем стандартный метод
            self.drag_and_drop(ingredient_locator, ConstructorLocators.CONSTRUCTOR_AREA)
    
    def _drag_and_drop_firefox(self, source_element, target_element):
        """Альтернативный метод перетаскивания для Firefox."""
        
        # Создаем новый экземпляр ActionChains
        actions = ActionChains(self.driver)
        
        # Перетаскивание с явными ожиданиями вместо time.sleep
        (actions
         .click_and_hold(source_element)
         .move_to_element(target_element)
         .release()
         .perform())
        
        # Ждем, пока счетчик обновится (максимум 5 секунд)
        WebDriverWait(self.driver, 5).until(
            lambda d: self.get_bun_counter_value() > 0
        )
    
    @allure.step("Добавить булку в конструктор")
    def add_bun_to_constructor(self, browser_name="chrome"):
        self.drag_ingredient_to_constructor(ConstructorLocators.BUN_INGREDIENT, browser_name)
    
    @allure.step("Получить значение счетчика булки")
    def get_bun_counter_value(self):
        return self.get_counter_value(ConstructorLocators.BUN_COUNTER)
    
    @allure.step("Проверить, что счетчик булки отображается")
    def is_bun_counter_visible(self):
        return self.is_element_visible(ConstructorLocators.BUN_COUNTER)
    
    @allure.step("Дождаться обновления счетчика")
    def wait_for_counter_update(self, initial_value, timeout=5):
        """Ждать, пока счетчик изменится от начального значения."""
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_bun_counter_value() != initial_value
        )