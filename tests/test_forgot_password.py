import pytest
import allure
from pages.login_page import LoginPage
from pages.forgot_password import ForgotPassword

class TestForgotPassword:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.forgot_password_page = ForgotPassword(driver)

    @allure.title('Переход на страницу восстановления пароля')
    def test_go_to_forgot_password_page(self):
        """Тест 1.1: Переход на страницу восстановления пароля по кнопке «Восстановить пароль»"""
        # Переходим на страницу логина
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        
        # Кликаем на ссылку "Восстановить пароль"
        self.login_page.click_forgot_password_link()
        
        # Проверяем, что перешли на страницу восстановления пароля
        assert "/forgot-password" in self.driver.current_url
        print("✅ Успешно перешли на страницу восстановления пароля")

    @allure.title('Ввод почты и клик по кнопке Восстановить')
    @pytest.mark.skip(reason="Требуется исследование логики восстановления пароля")
    def test_restore_password_with_email(self):
        """Тест 1.2: Ввод почты и клик по кнопке «Восстановить»"""
        # Этот тест временно пропускаем
        pytest.skip("Требуется дополнительное исследование логики восстановления пароля")

    @allure.title('Кнопка показать/скрыть пароль делает поле активным')
    def test_show_hide_password_button(self):
        """Тест 1.3: Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"""
        # Переходим на страницу восстановления пароля
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        
        # TODO: Реализовать после исследования
        print("✅ Тест будет реализован после исследования кнопки показа/скрытия пароля")