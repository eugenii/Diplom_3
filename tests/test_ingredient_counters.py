# test_ingredient_counters.py - максимально упрощенная версия
import allure
import pytest

from pages.constructor_page import ConstructorPage

@pytest.mark.usefixtures("driver")
class TestIngredientCounters:

    @allure.title("Проверка увеличения счетчика ингредиента при добавлении")
    def test_ingredient_counter_increases_when_added(self, driver):
        constructor_page = ConstructorPage(driver)
        
        # Переходим на главную страницу
        constructor_page.navigate_to_main()
        
        # Получаем начальное значение счетчика
        initial_counter = constructor_page.get_bun_counter_value()
        print(f"Начальное значение счетчика: {initial_counter}")
        
        # Добавляем булку в конструктор
        constructor_page.add_bun_to_constructor()
        
        # Ждем обновления счетчика
        constructor_page.wait_for_counter_update(initial_counter, timeout=10)
        
        # Получаем значение счетчика после добавления
        final_counter = constructor_page.get_bun_counter_value()
        print(f"Конечное значение счетчика: {final_counter}")
        
        # Проверяем, что счетчик увеличился
        assert final_counter > initial_counter, f"Счетчик не увеличился: было {initial_counter}, стало {final_counter}"