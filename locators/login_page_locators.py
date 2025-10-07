from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Локаторы для страницы логина."""
    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")