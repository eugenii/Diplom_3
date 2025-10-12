# [file name]: test_personal_account.py
# [file content begin]
import allure
import pytest
from data import LOGIN_URL, PERSONAL_ACCOUNT_URL, BASE_URL
from data import TestUser
from pages.login_page import LoginPage
from pages.personal_account import PersonalAccount

@pytest.mark.usefixtures("driver")
class TestPersonalAccount:
    """Тесты для личного кабинета."""
    
    def _login_user(self, driver):
        """Вспомогательный метод для авторизации пользователя."""
        login_page = LoginPage(driver)
        driver.get(LOGIN_URL)
        login_page.set_email(TestUser.EMAIL)
        login_page.set_password(TestUser.PASSWORD)
        login_page.click_login_button()
        return PersonalAccount(driver)
    
    @allure.feature("Личный кабинет")
    @allure.story("Переход по клику на «Личный кабинет»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_personal_account(self, driver):
        """2.1: Переход по клику на «Личный кабинет»."""
        
        with allure.step("Авторизовать пользователя"):
            personal_account = self._login_user(driver)
        
        with allure.step("Кликнуть на 'Личный кабинет'"):
            personal_account.click_personal_account_button()
        
        with allure.step("Проверить переход в личный кабинет"):
            assert "account" in driver.current_url, "Не удалось перейти в личный кабинет"
            assert personal_account.is_profile_page(), "Не открылась страница профиля"
            assert personal_account.is_user_authorized(), "Пользователь не авторизован"
    
    @allure.feature("Личный кабинет")
    @allure.story("Переход в раздел «История заказов»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_order_history(self, driver):
        """2.2: Переход в раздел «История заказов»."""
        
        with allure.step("Авторизовать пользователя"):
            personal_account = self._login_user(driver)
        
        with allure.step("Перейти в личный кабинет"):
            personal_account.click_personal_account_button()
            assert personal_account.is_profile_page(), "Не открылась страница профиля"
        
        with allure.step("Кликнуть на раздел 'История заказов'"):
            personal_account.click_order_history_section()
        
        with allure.step("Проверить переход в историю заказов"):
            assert personal_account.is_order_history_page(), "Не открылась история заказов"
            assert "account/order-history" in driver.current_url, "URL не соответствует истории заказов"
    
    @allure.feature("Личный кабинет")
    @allure.story("Выход из аккаунта")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_from_account(self, driver):
        """2.3: Выход из аккаунта."""
        
        with allure.step("Авторизовать пользователя"):
            personal_account = self._login_user(driver)
        
        with allure.step("Перейти в личный кабинет"):
            personal_account.click_personal_account_button()
            assert personal_account.is_profile_page(), "Не открылась страница профиля"
        
        with allure.step("Кликнуть на кнопку 'Выход'"):
            personal_account.click_logout_button()
        
        with allure.step("Проверить выход из аккаунта"):
            assert personal_account.is_logout_successful(), "Выход не выполнен - не открылась страница логина"
            assert "login" in driver.current_url, "URL не соответствует странице логина"
            
        with allure.step("Проверить, что нельзя вернуться в личный кабинет без авторизации"):
            driver.get(PERSONAL_ACCOUNT_URL)
            assert "login" in driver.current_url or personal_account.is_logout_successful(), \
                "Удалось получить доступ к личному кабинету без авторизации"
# [file content end]





# import allure
# import pytest
# from data import LOGIN_URL, PERSONAL_ACCOUNT_URL
# from data import TestUser
# from pages.login_page import LoginPage
# from pages.personal_account import PersonalAccount

# @pytest.mark.usefixtures("driver")
# class TestPersonalAccount:
#     """Тесты для личного кабинета."""
    
#     @allure.feature("Личный кабинет")
#     @allure.story("Переход по клику на «Личный кабинет»")
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_go_to_personal_account(self, driver):
#         """2.1: Переход по клику на «Личный кабинет»."""
#         # TODO: Реализовать после продолжения
#         pass
    
#     @allure.feature("Личный кабинет")
#     @allure.story("Переход в раздел «История заказов»")
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_go_to_order_history(self, driver):
#         """2.2: Переход в раздел «История заказов»."""
#         # TODO: Реализовать после продолжения
#         pass
    
#     @allure.feature("Личный кабинет")
#     @allure.story("Выход из аккаунта")
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_logout_from_account(self, driver):
#         """2.3: Выход из аккаунта."""
#         # TODO: Реализовать после продолжения
#         pass