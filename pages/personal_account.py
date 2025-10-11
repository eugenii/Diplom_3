from .base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
import allure

class PersonalAccount(BasePage):
    """Класс для работы с личным кабинетом."""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Кликнуть на 'Личный кабинет'")
    def click_personal_account_button(self):
        """Кликнуть на кнопку личного кабинета в хедере."""
        self.click_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Кликнуть на 'История заказов'")
    def click_order_history_section(self):
        """Кликнуть на раздел истории заказов."""
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_SECTION)
    
    @allure.step("Кликнуть на 'Выход'")
    def click_logout_button(self):
        """Кликнуть на кнопку выхода."""
        self.click_element(PersonalAccountLocators.LOGOUT_BUTTON)
    
    @allure.step("Проверить, что открыт профиль")
    def is_profile_page(self):
        """Проверить, что открыта страница профиля."""
        return self.is_element_visible(PersonalAccountLocators.PROFILE_HEADER)
    
    @allure.step("Проверить, что открыта история заказов")
    def is_order_history_page(self):
        """Проверить, что открыта страница истории заказов."""
        return self.is_element_visible(PersonalAccountLocators.ORDER_HISTORY_HEADER)