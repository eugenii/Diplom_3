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
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    
    # Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

    # Подтверждение выхода
    LOGIN_HEADER_AFTER_LOGOUT = (By.XPATH, "//h2[text()='Вход']")
    
    # Элементы для проверки авторизации
    USER_NAME_IN_PROFILE = (By.XPATH, "//input[@name='Name']")
    
    # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")