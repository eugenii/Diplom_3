import allure
import pytest

from data import BASE_URL
from pages.constructor_page import ConstructorPage

@pytest.mark.usefixtures("driver")
class TestIngredientCounters:
    
    @allure.title("3.5: Каунтер ингредиента увеличивается при добавлении в заказ")
    def test_ingredient_counter_increases_when_added(self, driver):
        constructor_page = ConstructorPage(driver)
        driver.get(BASE_URL)
        
        initial_bun_counter = constructor_page.get_bun_counter()
        initial_sauce_counter = constructor_page.get_sauce_counter()
        initial_filling_counter = constructor_page.get_filling_counter()
        
        constructor_page.add_bun_to_constructor()
        bun_counter_after = constructor_page.get_bun_counter()
        assert bun_counter_after > initial_bun_counter
        
        constructor_page.add_sauce_to_constructor()
        sauce_counter_after = constructor_page.get_sauce_counter()
        assert sauce_counter_after > initial_sauce_counter
        
        constructor_page.add_filling_to_constructor()
        filling_counter_after = constructor_page.get_filling_counter()
        assert filling_counter_after > initial_filling_counter