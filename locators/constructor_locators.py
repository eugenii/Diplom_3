# [file name]: locators/constructor_locators.py
# [file content begin]
from selenium.webdriver.common.by import By

class ConstructorLocators:
    """Локаторы для конструктора бургеров и каунтеров."""
    
    # Ингредиенты
    BUN_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[1]")  # Первая булка
    SAUCE_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[4]")  # Первый соус
    FILLING_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[7]")  # Первая начинка
    
    # Каунтеры ингредиентов (правильные локаторы из диагностики)
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter__ZNLkj')]//p[contains(@class, 'counter_counter__num__3nue1')]")
    
    # Конструктор бургера (зона drop)
    CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]")
    
    # Кнопка оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]")
    
    # Элементы для проверки авторизации перед заказом
    LOGIN_BUTTON_IN_CONSTRUCTOR = (By.XPATH, "//button[text()='Войти в аккаунт']")
# [file content end]