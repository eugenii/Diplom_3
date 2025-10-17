from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Перейти на страницу ленты заказов")
    def navigate_to_order_feed(self):
        self.navigate_to("https://stellarburgers.education-services.ru/feed")
    
    @allure.step("Проверить, что лента заказов загрузилась")
    def wait_for_order_feed_loaded(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(OrderFeedLocators.ORDER_FEED_SECTION)
        )
    
    @allure.step("Дождаться появления заказов в ленте")
    def wait_for_orders_appear(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(OrderFeedLocators.ORDER_LINKS)
        )
    
    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order(self):
        try:
            first_order = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(OrderFeedLocators.FIRST_ORDER_LINK)
            )
            first_order.click()
            return True
        except:
            try:
                first_order = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(OrderFeedLocators.FIRST_ORDER_CARD)
                )
                first_order.click()
                return True
            except:
                return False
    
    @allure.step("Проверить, что модальное окно деталей заказа открылось")
    def is_order_modal_opened(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(OrderFeedLocators.ORDER_DETAILS_MODAL)
            )
            return True
        except:
            return False
    
    @allure.step("Закрыть модальное окно")
    def close_order_modal(self, timeout=5):
        try:
            close_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(OrderFeedLocators.MODAL_CLOSE_BUTTON)
            )
            close_button.click()
            
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(OrderFeedLocators.ORDER_DETAILS_MODAL)
            )
            return True
        except:
            return False
    
    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrderFeedLocators.TOTAL_ORDERS_COUNT)
            )
            return int(element.text)
        except:
            return 0
    
    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrderFeedLocators.TODAY_ORDERS_COUNT)
            )
            return int(element.text)
        except:
            return 0
    
    @allure.step("Дождаться увеличения общего количества заказов")
    def wait_for_total_orders_increase(self, initial_count, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_total_orders_count() > initial_count
        )
    
    @allure.step("Дождаться увеличения количества заказов за сегодня")
    def wait_for_today_orders_increase(self, initial_count, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_today_orders_count() > initial_count
        )
    
    @allure.step("Получить количество заказов по локатору XPath")
    def get_orders_count_by_xpath(self, xpath_locator):
        elements = self.driver.find_elements(By.XPATH, xpath_locator)
        return len(elements)