BASE_URL = "https://stellarburgers.education-services.ru"
LOGIN_URL = "https://stellarburgers.education-services.ru/login"
FORGOT_PASSWORD_URL = "https://stellarburgers.education-services.ru/forgot-password"
# URL для личного кабинета
PERSONAL_ACCOUNT_URL = "https://stellarburgers.education-services.ru/account"

# Тестовые данные пользователя
class TestUser:
    # TODO: Замените на реальные данные существующего пользователя
    EMAIL = "1234@g.ru"
    PASSWORD = "12345678qwerty"
    NAME = "1234@g.ru"

# Тестовые данные для восстановления пароля
class TestForgotPasswordData:
    # Используем существующий email или тестовый
    EXISTING_EMAIL = "1234@g.ru"
    INVALID_EMAIL = "invalid_email@test.ru"
    NON_EXISTENT_EMAIL = "nonexistent@test.ru"