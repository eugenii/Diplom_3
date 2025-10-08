from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    """Локаторы для страницы восстановления пароля."""
    
    # Поле для ввода email (исправлено)
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    
    # Кнопка "Восстановить" (исправлено)
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    
    # Кнопка показать/скрыть пароль (глазик)
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")