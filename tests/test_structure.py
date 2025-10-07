import pytest
from pages.main_page import MainPage

def test_basic_structure(driver):
    """Простой тест для проверки что структура работает."""
    main_page = MainPage(driver)
    
    # Просто проверяем что страница загрузилась
    assert "stellarburgers" in driver.current_url
    print("Базовая структура работает! Можно продолжать.")