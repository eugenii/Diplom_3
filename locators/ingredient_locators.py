from selenium.webdriver.common.by import By

class IngredientLocators:
    """Локаторы для работы с модальными окнами ингредиентов."""
    
    # Ингредиенты
    ANY_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[1]")
    
    # Модальное окно
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    
    # Кнопка закрытия (крестик)
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
