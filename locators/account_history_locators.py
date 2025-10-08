from selenium.webdriver.common.by import By

class AccountHistoryLocators:
    """Локаторы для страницы истории заказов."""
    # Заголовок "История заказов"
    HISTORY_HEADER = (By.XPATH, "//h1[text()='История заказов']")
    
    # Ссылка "Профиль" (для возврата)
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")