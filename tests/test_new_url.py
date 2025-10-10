# tests/test_new_url.py
def test_new_url_accessible(driver):
    """Проверка доступности нового URL"""
    driver.get("https://stellarburgers.education-services.ru/")
    assert "Stellar Burgers" in driver.title
    print("✅ Новый URL доступен")