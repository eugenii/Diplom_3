from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    """Локаторы для личного кабинета."""
    
    # Кнопка "Личный кабинет" в хедере
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Разделы личного кабинета
    PROFILE_SECTION = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_SECTION = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # Упрощенные проверки для личного кабинета
    PROFILE_HEADER = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_HEADER = (By.XPATH, "//a[text()='История заказов']")
    
    # Навигация в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    
    # Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    # Подтверждение выхода
    LOGIN_HEADER_AFTER_LOGOUT = (By.XPATH, "//h2[text()='Вход']")
    
    # Элементы для проверки авторизации
    USER_NAME_IN_PROFILE = (By.XPATH, "//input[@name='Name']")
    
    # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Общие проверки для личного кабинета
    ACCOUNT_PAGE_INDICATOR = (By.XPATH, "//a[text()='Профиль']")
