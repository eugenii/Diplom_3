import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage

class TestOrderFlow:
    
    @allure.title("3.6: Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_create_order(self, driver, login_user):
        main_page = MainPage(driver)
        
        main_page.add_bun_to_constructor()
        main_page.add_sauce_to_constructor()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )
        order_button.click()
        
        order_modal = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal__container')]"))
        )
        assert order_modal.is_displayed()