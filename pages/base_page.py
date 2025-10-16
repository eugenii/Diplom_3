from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from data import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
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
        
    def wait_for_url(self, url, timeout=10):
        """Ожидание появления URL."""
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))

    def drag_and_drop(self, source_locator, target_locator):
        """Перетащить элемент из source в target."""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()
    
    def get_counter_value(self, counter_locator):
        """Получить значение каунтера."""
        try:
            counter = self.find_element(counter_locator)
            return int(counter.text)
        except:
            return 0
        
    def click_element_js(self, locator):
        """Кликнуть по элементу через JavaScript."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    def safe_click(self, locator, use_js=False):
        """Безопасный клик с возможностью использовать JavaScript."""
        if use_js:
            self.click_element_js(locator)
        else:
            self.click_element(locator)

    def wait_for_modal_to_disappear(self, timeout=10):
        """Ожидать исчезновение модального окна."""
        try:
            # Сначала проверяем, есть ли модальное окно
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
            )
            # Если есть - ждем его исчезновения
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
            )
            print("✅ Модальное окно исчезло")
            return True
        except TimeoutException:
            # Если модальное окно не появилось или не исчезло - это нормально
            print("ℹ️ Модальное окно не найдено или не исчезло")
            return False

    def safe_click_with_modal_check(self, locator, browser_name="chrome"):
        """Безопасный клик с проверкой модального окна для Firefox."""
        if browser_name.lower() == "firefox":
            print(f"🦊 Firefox: Обработка клика для {locator}")
            
            # Для Firefox используем комбинированный подход
            # 1. Ждем исчезновения модального окна
            self.wait_for_modal_to_disappear(8)
            
            # 2. Всегда используем JS клик для надежности
            self.click_element_js(locator)
            print("✅ JS клик выполнен успешно")
            
        else:
            # Для Chrome обычный клик
            self.click_element(locator)