from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Локаторы для страницы логина."""
    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")

        # Добавляем для авторизации:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
