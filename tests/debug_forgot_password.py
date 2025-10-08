# tests/debug_forgot_password.py
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.forgot_password import ForgotPassword

def test_debug_forgot_password(driver):
    """Тест для отладки процесса восстановления пароля"""
    
    # 1. Переходим на страницу логина
    login_page = LoginPage(driver)
    driver.get("https://stellarburgers.nomoreparties.site/login")
    
    print("✅ Перешли на страницу логина")
    
    # 2. Кликаем "Восстановить пароль"
    login_page.click_forgot_password_link()
    
    print("✅ Кликнули на 'Восстановить пароль'")
    print(f"Текущий URL: {driver.current_url}")
    
    # 3. Работаем со страницей восстановления
    forgot_password_page = ForgotPassword(driver)
    
    # Проверяем, что мы на правильной странице
    assert "/forgot-password" in driver.current_url, "Не перешли на страницу восстановления пароля"
    
    # Проверяем наличие элементов на странице
    print("Проверяем наличие элементов на странице...")
    
    # Проверяем поле email
    try:
        email_field = forgot_password_page.find_element(forgot_password_page.locators.EMAIL_INPUT)
        print("✅ Поле email найдено")
    except:
        print("❌ Поле email НЕ найдено")
        driver.save_screenshot("debug_email_field.png")
    
    # Проверяем кнопку восстановления
    try:
        restore_button = forgot_password_page.find_element(forgot_password_page.locators.RESTORE_BUTTON)
        print("✅ Кнопка 'Восстановить' найдена")
    except:
        print("❌ Кнопка 'Восстановить' НЕ найдена")
        driver.save_screenshot("debug_restore_button.png")
    
    # Пробуем ввести email и нажать кнопку
    print("Пробуем ввести email и нажать кнопку...")
    forgot_password_page.set_email("test@example.com")  # Используем тестовый email
    forgot_password_page.click_restore_button()
    
    # Ждем и проверяем URL
    time.sleep(3)
    print(f"Текущий URL после восстановления: {driver.current_url}")
    
    # Проверяем, перешли ли на страницу сброса пароля
    if "/reset-password" in driver.current_url:
        print("✅ Успешно перешли на страницу сброса пароля!")
    else:
        print("❌ Не перешли на страницу reset-password")
        print("Возможные причины:")
        print("1. Email не зарегистрирован в системе")
        print("2. Проблема с логикой восстановления")
        print("3. Нужно проверить сообщения на странице")