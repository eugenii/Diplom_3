# ingredient_page.py - добавляем безопасные клики и ожидания
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from locators.ingredient_locators import IngredientLocators


class IngredientPage(BasePage):
    """Класс для работы с модальными окнами ингредиентов."""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Перейти на главную страницу")
    def navigate_to_main(self):
        """Перейти на главную страницу."""
        self.navigate_to_home()
    
    @allure.step("Кликнуть на любой ингредиент")
    def click_any_ingredient(self):
        """Кликнуть на первый доступный ингредиент."""
        # Используем безопасный клик для Firefox
        browser_name = self.get_browser_name()
        self.safe_click_with_modal_check(IngredientLocators.ANY_INGREDIENT, browser_name)
        
        # Ждем появления модального окна
        self.wait_for_modal_opened()
    
    @allure.step("Дождаться открытия модального окна")
    def wait_for_modal_opened(self, timeout=10):
        """Дождаться открытия модального окна."""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(IngredientLocators.MODAL_CONTENT)
        )
    
    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self):
        """Проверить, что модальное окно открыто."""
        return self.is_element_visible(IngredientLocators.MODAL_CONTENT)
    
    @allure.step("Кликнуть на кнопку закрытия модального окна")
    def click_modal_close_button(self):
        """Кликнуть на крестик для закрытия модального окна."""
        # Используем безопасный клик для Firefox
        browser_name = self.get_browser_name()
        self.safe_click_with_modal_check(IngredientLocators.MODAL_CLOSE_BUTTON, browser_name)
        
        # Ждем закрытия модального окна
        self.wait_for_modal_closed()
    
    @allure.step("Дождаться закрытия модального окна")
    def wait_for_modal_closed(self, timeout=10):
        """Дождаться закрытия модального окна."""
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(IngredientLocators.MODAL_CONTENT)
        )
    
    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        """Проверить, что модальное окно закрыто."""
        return not self.is_element_visible(IngredientLocators.MODAL_CONTENT)