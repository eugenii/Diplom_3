import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.constructor_page import ConstructorPage
from locators.constructor_locators import ConstructorLocators


@pytest.mark.usefixtures("driver")
class TestIngredientCounters:

    @allure.title("Проверка увеличения счетчика ингредиента при добавлении")
    def test_ingredient_counter_increases_when_added(self, driver):
        constructor_page = ConstructorPage(driver)
        
        # Определяем имя браузера
        browser_name = driver.capabilities['browserName']
        
        # Получаем начальное значение счетчика
        initial_counter = constructor_page.get_bun_counter_value()
        
        # Добавляем булку в конструктор
        constructor_page.add_bun_to_constructor(browser_name)
        
        # Ждем обновления счетчика
        constructor_page.wait_for_counter_update(initial_counter, timeout=10)
        
        # Получаем значение счетчика после добавления
        final_counter = constructor_page.get_bun_counter_value()
        
        # Проверяем, что счетчик увеличился
        assert final_counter > initial_counter, f"Счетчик не увеличился: было {initial_counter}, стало {final_counter}"