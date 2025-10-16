# Diplom_3
Часть 3 дипломного проекта Q_A python

Тесты для chrome работают корректно, для firefox только для восстановления пароля.

В работе использована модель Page Object. Тесты разбиты на блоки в соответствие с заданием. 

Работа с разными браузерами заложена в параметризованной фикстуре в conftest.py
# Autotests for Stellar Burgers


## 📋 О проекте

Автотесты для веб-приложения "Stellar Burgers" - сервиса заказа бургеров. Тесты покрывают ключевые сценарии работы с пользователем и конструктором бургеров.

##  Возможности

- **Тестирование авторизации** - вход, восстановление пароля
- **Работа с конструктором** - добавление ингредиентов, проверка счетчиков
- **Кросбраузерное тестирование** - поддержка Chrome и Firefox
- **Page Object Pattern** - чистая и поддерживаемая структура кода
- **Allure отчеты** - детальная визуализация результатов тестов

## Технологии

- **Python 3.13** - основной язык программирования
- **Selenium WebDriver** - автоматизация браузера
- **Pytest** - фреймворк для тестирования
- **Allure Framework** - создание отчетов
- **Page Object Pattern** - архитектура тестов

## Структура проекта
Diplom_3/
├── pages/ # Page Object классы
│ ├── base_page.py
│ ├── login_page.py
│ └── constructor_page.py
├── locators/ # Локаторы элементов
│ ├── login_locators.py
│ └── constructor_locators.py
├── tests/ # Тестовые сценарии
│ ├── test_forgot_password.py
│ └── test_ingredient_counters.py
├── data.py # Тестовые данные
├── conftest.py # Pytest фикстуры
└── requirements.txt # Зависимости



### Установка зависимостей
```bash
pip install -r requirements.txt

### Запуск тестов
pytest   // просто все
pytest --alluredir=allure-results  // с генерацией отчета
allure serve allure-results   // просмотр отчета

Запуск тестов для конкретного браузера
bash
# Только Chrome
pytest -k "chrome"

# Только Firefox  
pytest -k "firefox"