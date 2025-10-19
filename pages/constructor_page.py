# constructor_page.py - полностью переписываем без сложных локаторов
from .base_page import BasePage
from locators.constructor_locators import ConstructorLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Дождаться загрузки конструктора")
    def wait_for_constructor_loaded(self, timeout=10):
        """Дождаться загрузки конструктора по простому локатору."""
        # Используем простой локатор, который точно есть
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
        )
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self, browser_name="chrome"):
        # Сначала ждем загрузки конструктора
        self.wait_for_constructor_loaded()
        
        # Находим первый ингредиент (простой локатор)
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//a[contains(@href, 'ingredient')])[1]"))
        )
        
        # Находим область конструктора (простой локатор)
        constructor_area = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"))
        )
        
        # Выполняем перетаскивание
        actions = ActionChains(self.driver)
        (actions
         .click_and_hold(ingredient)
         .move_to_element(constructor_area)
         .release()
         .perform())
    
    @allure.step("Добавить булку в конструктор")
    def add_bun_to_constructor(self, browser_name="chrome"):
        # Просто перетаскиваем ингредиент
        self.drag_ingredient_to_constructor(browser_name)
    
    @allure.step("Получить значение счетчика булки")
    def get_bun_counter_value(self):
        try:
            # Простой локатор для счетчика
            return self.get_counter_value((By.XPATH, "(//p[contains(@class, 'counter__num')])[1]"))
        except:
            return 0
    
    @allure.step("Дождаться обновления счетчика")
    def wait_for_counter_update(self, initial_value, timeout=10):
        """Ждать, пока счетчик изменится от начального значения."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: self.get_bun_counter_value() != initial_value
            )
            return True
        except:
            return False
    
    @allure.step("Перейти на главную страницу")
    def navigate_to_main(self):
        """Перейти на главную страницу."""
        self.navigate_to_home()
        self.wait_for_constructor_loaded()