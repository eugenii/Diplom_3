import allure
import pytest

from data import BASE_URL
# from pages.main_page import MainPage
from pages.ingredient_page import IngredientPage

@pytest.mark.usefixtures("driver")
class TestIngredientModals:
    
    @allure.title("3.3: Клик на ингредиент открывает модальное окно")
    def test_click_ingredient_opens_modal(self, driver):
        driver.get(BASE_URL)
        # main_page = MainPage(driver)
        ingredient_page = IngredientPage(driver)
        
        ingredient_page.click_any_ingredient()
        assert ingredient_page.is_modal_opened()
    
    @allure.title("3.4: Модальное окно закрывается кликом на крестик")
    def test_modal_closes_with_close_button(self, driver):
        driver.get(BASE_URL)
        ingredient_page = IngredientPage(driver)
        
        ingredient_page.click_any_ingredient()
        ingredient_page.click_modal_close_button()
        
        assert ingredient_page.is_modal_closed()