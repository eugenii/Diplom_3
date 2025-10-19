# test_ingredient_modals.py - заменяем navigate_to_main на navigate_to_home
import allure
import pytest

from data import BASE_URL
from pages.ingredient_page import IngredientPage

@pytest.mark.usefixtures("driver")
class TestIngredientModals:
    
    @allure.title("3.3: Клик на ингредиент открывает модальное окно")
    def test_click_ingredient_opens_modal(self, driver):
        ingredient_page = IngredientPage(driver)
        
        # Переходим на главную страницу через метод страницы (исправляем метод)
        ingredient_page.navigate_to_home()
        
        # Кликаем на ингредиент через метод страницы
        ingredient_page.click_any_ingredient()
        
        # Проверяем через метод страницы
        assert ingredient_page.is_modal_opened()
    
    @allure.title("3.4: Модальное окно закрывается кликом на крестик")
    def test_modal_closes_with_close_button(self, driver):
        ingredient_page = IngredientPage(driver)
        
        # Переходим на главную страницу через метод страницы (исправляем метод)
        ingredient_page.navigate_to_home()
        
        # Открываем модальное окно через метод страницы
        ingredient_page.click_any_ingredient()
        
        # Закрываем модальное окно через метод страницы
        ingredient_page.click_modal_close_button()
        
        # Проверяем через метод страницы
        assert ingredient_page.is_modal_closed()