from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы (конструктор)."""
    
    # Кнопка "Личный Кабинет" в хедере
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    
    # Кнопка "Лента заказов"
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    
    # Локаторы для модального окна
    # Первый ингредиент в списке (булка)
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[1]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]")
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")

    # Исправленный локатор для крестика
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")

    # Локаторы для конструктора (область куда перетаскивать)
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")

    # Локаторы для каунтеров ингредиентов
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num__3nue1')]")

    # Локаторы для конкретных ингредиентов (пример)
    BUN_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[1]")
    SAUCE_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[6]")
    MAIN_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[11]")

    # Локаторы для каунтеров
    BUN_COUNTER = (By.XPATH, "(//section[h2[text()='Булки']]//p[contains(@class, 'counter_counter__num__3nue1')])[1]")