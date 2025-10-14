# [file name]: locators/ingredient_locators.py
# [file content begin]
from selenium.webdriver.common.by import By

class IngredientLocators:
    """Локаторы для работы с модальными окнами ингредиентов."""
    
    # Ингредиенты - правильные локаторы из диагностики
    ANY_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[1]")
    
    # Модальное окно - правильные локаторы из диагностики
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    
    # Кнопка закрытия (крестик) - правильный локатор из диагностики
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
# [file content end]