from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site"
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Найти элемент с ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def input_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text
    
    def wait_for_url_contains(self, text):
        """Ожидать, что URL содержит текст"""
        self.wait.until(EC.url_contains(text))
    
    def is_element_visible(self, locator):
        """Проверить, что элемент видим"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False