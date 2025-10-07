from selenium.webdriver.common.by import By

class AccountProfileLocators:
    """Локаторы для страницы профиля в личном кабинете."""
    
    # Заголовок "Профиль"
    PROFILE_HEADER = (By.XPATH, "//a[text()='Профиль']")
    
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")