# personal_account.py - добавляем недостающие методы
import allure

from .base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccount(BasePage):
    """Класс для работы с личным кабинетом."""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Кликнуть на 'Личный кабинет'")
    def click_personal_account_button(self):
        """Кликнуть на кнопку личного кабинета в хедере."""
        browser_name = self.get_browser_name()
        return self.safe_click_with_modal_check(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON, browser_name)

    @allure.step("Кликнуть на 'Профиль'")
    def click_profile_section(self):
        """Кликнуть на раздел профиля."""
        self.click_element(PersonalAccountLocators.PROFILE_SECTION)
    
    @allure.step("Кликнуть на 'История заказов'")
    def click_order_history_section(self):
        """Кликнуть на раздел истории заказов."""
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_SECTION)

    @allure.step("Кликнуть на 'Выход'")
    def click_logout_button(self):
        """Кликнуть на кнопку выхода."""
        browser_name = self.get_browser_name()
        return self.safe_click_with_modal_check(PersonalAccountLocators.LOGOUT_BUTTON, browser_name)
    
    @allure.step("Проверить, что открыт профиль")
    def is_profile_page(self):
        """Проверить, что открыта страница профиля."""
        return self.is_element_visible(PersonalAccountLocators.PROFILE_SECTION)
    
    @allure.step("Проверить, что открыта история заказов")
    def is_order_history_page(self):
        """Проверить, что открыта страница истории заказов."""
        return self.is_element_visible(PersonalAccountLocators.ORDER_HISTORY_SECTION)
    
    @allure.step("Проверить, что пользователь авторизован")
    def is_user_authorized(self):
        """Проверить авторизацию по наличию поля имени в профиле."""
        return self.is_element_visible(PersonalAccountLocators.USER_NAME_IN_PROFILE)
    
    @allure.step("Проверить выход из аккаунта")
    def is_logout_successful(self):
        """Проверить, что выход выполнен успешно (открыта страница логина)."""
        return self.is_element_visible(PersonalAccountLocators.LOGIN_HEADER_AFTER_LOGOUT)
    
    # ДОБАВЛЯЕМ НЕДОСТАЮЩИЕ МЕТОДЫ:
    @allure.step("Проверить, что находимся на странице аккаунта")
    def is_on_account_page(self):
        """Проверить, что находимся на странице аккаунта по URL."""
        return self.is_url_contains("account")
    
    @allure.step("Проверить, что находимся на странице логина")
    def is_on_login_page(self):
        """Проверить, что находимся на странице логина по URL."""
        return self.is_url_contains("login")
    
    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor_button(self):
        """Кликнуть на кнопку конструктора в хедере."""
        self.click_element(PersonalAccountLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Кликнуть на логотип")
    def click_logo_button(self):
        """Кликнуть на логотип Stellar Burgers."""
        self.click_element(PersonalAccountLocators.LOGO_BUTTON)
    
    @allure.step("Кликнуть на 'Войти в аккаунт' на главной")
    def click_login_button_main(self):
        """Кликнуть на кнопку входа на главной странице."""
        self.click_element(PersonalAccountLocators.LOGIN_BUTTON_MAIN)