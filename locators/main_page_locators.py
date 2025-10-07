from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы (конструктор)."""
    
    # Кнопка "Личный Кабинет" в хедере
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    
    # Кнопка "Лента заказов"
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента заказов']")
    
    # Кнопка "Войти в аккаунт" на главной
    # LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")