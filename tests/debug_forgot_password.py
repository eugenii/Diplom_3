import pytest
import time
from pages.login_page import LoginPage
from pages.forgot_password import ForgotPassword

def test_debug_forgot_password(driver):
    """Тест для отладки процесса восстановления пароля"""
    # Переходим на страницу восстановления пароля
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    
    forgot_password_page = ForgotPassword(driver)
    
    # Проверяем, что элементы присутствуют
    print("Проверяем наличие элементов на странице...")
    
    # Проверяем поле email
    try:
        email_field = forgot_password_page.find_element(forgot_password_page.locators.EMAIL_INPUT)
        print("✅ Поле email найдено")
    except:
        print("❌ Поле email НЕ найдено")
        # Сделаем скриншот
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
    forgot_password_page.set_email("valid_user@yandex.ru")  # Попробуем с другим email
    forgot_password_page.click_restore_button()
    
    # Ждем и проверяем URL
    time.sleep(3)
    print(f"Текущий URL: {driver.current_url}")
    
    # Если остались на той же странице, проверим есть ли сообщения об ошибке
    if "/reset-password" not in driver.current_url:
        print("Не перешли на страницу reset-password. Возможные причины:")
        print("1. Email не зарегистрирован в системе")
        print("2. Требуется дополнительная проверка")
        print("3. Логика восстановления пароля изменилась")
        
        # Посмотрим на HTML страницы
        page_source = driver.page_source
        if "error" in page_source.lower() or "ошибка" in page_source.lower():
            print("На странице есть сообщение об ошибке")
        else:
            print("Явных сообщений об ошибке нет")