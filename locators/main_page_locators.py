from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы."""

    CABINET_LOCATOR = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"
