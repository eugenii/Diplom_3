from selenium.webdriver.common.by import By

class IngredientLocators:
    """Локаторы для работы с модальными окнами ингредиентов."""
    
    # Любой ингредиент для клика
    ANY_INGREDIENT = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]//a[1]")
    
    # Модальное окно
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal_content')]")
    
    # Кнопка закрытия (крестик)
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal_header')]//button")
