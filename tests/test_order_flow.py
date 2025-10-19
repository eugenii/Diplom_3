# test_order_flow.py - убираем WebDriverWait
import allure
import pytest

from pages.main_page import MainPage

class TestOrderFlow:
    
    @allure.title("3.6: Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_create_order(self, driver, login_user):
        main_page = MainPage(driver)
        
        main_page.add_bun_to_constructor()
        main_page.add_sauce_to_constructor()
        
        # Заменяем WebDriverWait на метод Page Object
        main_page.click_order_button()
        
        # Заменяем WebDriverWait на метод Page Object
        assert main_page.is_order_modal_displayed()