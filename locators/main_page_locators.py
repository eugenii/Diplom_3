from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы и навигации."""
    
    # Основная навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Активные разделы (для проверки)
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
    
    # Заголовки для проверки
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Ингредиенты
    INGREDIENTS_SECTION = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]")
    
    # Конструктор бургера
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")