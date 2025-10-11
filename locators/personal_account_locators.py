from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    """Локаторы для личного кабинета."""
    
    # Кнопка "Личный кабинет" в хедере
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    
    # Разделы личного кабинета
    PROFILE_SECTION = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_SECTION = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # Элементы профиля
    PROFILE_HEADER = (By.XPATH, "//h2[text()='Профиль']")
    ORDER_HISTORY_HEADER = (By.XPATH, "//h2[text()='История заказов']")
    
    # Кнопка "Конструктор" в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")
    
    # Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")