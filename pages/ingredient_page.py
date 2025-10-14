# [file name]: pages/ingredient_page.py
# [file content begin]
from .base_page import BasePage
from locators.ingredient_locators import IngredientLocators
import allure
import time

class IngredientPage(BasePage):
    """Класс для работы с модальными окнами ингредиентов."""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Кликнуть на любой ингредиент")
    def click_any_ingredient(self):
        """Кликнуть на первый доступный ингредиент."""
        self.click_element(IngredientLocators.ANY_INGREDIENT)
        time.sleep(2)  # Ждем появления модалки
    
    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self):
        """Проверить, что модальное окно открыто."""
        return self.is_element_visible(IngredientLocators.MODAL_CONTENT)
    
    @allure.step("Кликнуть на кнопку закрытия модального окна")
    def click_modal_close_button(self):
        """Кликнуть на крестик для закрытия модального окна."""
        self.click_element(IngredientLocators.MODAL_CLOSE_BUTTON)
        time.sleep(1)  # Ждем закрытия
    
    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        """Проверить, что модальное окно закрыто."""
        return not self.is_element_visible(IngredientLocators.MODAL_CONTENT)
# [file content end]