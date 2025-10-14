# [file name]: locators/forgot_password_locators.py
from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    """Локаторы для страницы восстановления пароля."""
    
    # Основные локаторы
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    
    # Локаторы для страницы сброса пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    
    # Универсальный локатор для контейнера пароля (ищет по полю ввода внутри)
    PASSWORD_CONTAINER = (By.XPATH, "//input[@name='Введите новый пароль']/parent::div")
    
    EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    
    # Заголовки
    FORGOT_PASSWORD_HEADER = (By.XPATH, "//h2[contains(text(), 'Восстановление')]")
    RESET_PASSWORD_HEADER = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")