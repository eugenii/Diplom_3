from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    """Локаторы для страницы восстановления пароля."""
    
    # Основные локаторы
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    
    # Локаторы для страницы сброса пароля (на основе диагностики)
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password' and @name='Введите новый пароль']")
    PASSWORD_CONTAINER = (By.XPATH, "//div[contains(@class, 'input_type_password')]")
    EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    
    # Заголовки
    FORGOT_PASSWORD_HEADER = (By.XPATH, "//h2[contains(text(), 'Восстановление')]")
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'ссылка для восстановления пароля')]")