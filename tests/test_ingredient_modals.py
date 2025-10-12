import allure
import pytest
from data import BASE_URL
from pages.main_page import MainPage
from pages.ingredient_page import IngredientPage

@pytest.mark.usefixtures("driver")
class TestIngredientModals:
    """Минимальные тесты для модальных окон ингредиентов."""
    
    @allure.feature("Основной функционал")
    @allure.story("Клик на ингредиент открывает модальное окно")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_ingredient_opens_modal(self, driver):
        """3.3: Если кликнуть на ингредиент, появится всплывающее окно."""
        
        with allure.step("Перейти на главную страницу"):
            driver.get(BASE_URL)
            main_page = MainPage(driver)
            assert main_page.is_constructor_opened()
        
        with allure.step("Кликнуть на любой ингредиент"):
            ingredient_page = IngredientPage(driver)
            ingredient_page.click_any_ingredient()
        
        with allure.step("Проверить открытие модального окна"):
            assert ingredient_page.is_modal_opened(), "Модальное окно не открылось"
    
    @allure.feature("Основной функционал")
    @allure.story("Модальное окно закрывается кликом на крестик")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_modal_closes_with_close_button(self, driver):
        """3.4: Всплывающее окно закрывается кликом по крестику."""
        
        with allure.step("Перейти на главную страницу"):
            driver.get(BASE_URL)
            main_page = MainPage(driver)
            assert main_page.is_constructor_opened()
        
        with allure.step("Открыть модальное окно ингредиента"):
            ingredient_page = IngredientPage(driver)
            ingredient_page.click_any_ingredient()
            assert ingredient_page.is_modal_opened()
        
        with allure.step("Кликнуть на крестик"):
            ingredient_page.click_modal_close_button()
        
        with allure.step("Проверить закрытие модального окна"):
            assert ingredient_page.is_modal_closed(), "Модальное окно не закрылось"
