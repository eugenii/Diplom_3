from selenium.webdriver.common.by import By


class ConstructorLocators:
    """Локаторы для страницы конструктора бургеров."""
    
    # Область конструктора (более надежный локатор)
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__list')]")
    
    # Ингредиенты
    BUN_INGREDIENT = (By.XPATH, "//a[contains(@href, 'ingredient/61c0c5a71d1f82001bdaaa6d') and contains(@class, 'BurgerIngredient_ingredient')]")
    
    # Счетчики (более надежный локатор)
    BUN_COUNTER = (By.XPATH, "//a[contains(@href, 'ingredient/61c0c5a71d1f82001bdaaa6d')]//p[contains(@class, 'counter__num')]")