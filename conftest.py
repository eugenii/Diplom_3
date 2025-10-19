import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import BASE_URL

@pytest.fixture(params=["chrome", "firefox"])  # Только Chrome - РАБОЧИЙ вариант
def driver(request):
    browser_name = request.param
    driver = None
    
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        # firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    
    driver.implicitly_wait(10)
    with allure.step(f"Открытие браузера {browser_name}"):
        driver.get(BASE_URL)
    
    yield driver
    
    with allure.step("Закрытие браузера"):
        driver.quit()

@pytest.fixture
def login_user(driver):
    """
    Фикстура для логина пользователя перед тестами заказов.
    """
    from data import TestUser
    from pages.login_page import LoginPage
    from locators.main_page_locators import MainPageLocators
    
    with allure.step("Логин пользователя"):
        login_page = LoginPage(driver)
        driver.get("https://stellarburgers.education-services.ru/login")
        
        login_page.set_email(TestUser.EMAIL)
        login_page.set_password(TestUser.PASSWORD)
        login_page.click_login_button()
        
        # Ждём перехода на главную
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )
        
        yield