import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=["chrome"])  # , "firefox"
def driver(request):
    browser_name = request.param
    driver = None
    
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--headless")  # раскомментируйте для headless режима
        driver = webdriver.Chrome(options=chrome_options)
    # elif browser_name == "firefox":
    #     firefox_options = FirefoxOptions()
    #     firefox_options.add_argument("--width=1920")
    #     firefox_options.add_argument("--height=1080")
    #     # firefox_options.add_argument("--headless")  # раскомментируйте для headless режима
    #     driver = webdriver.Firefox(options=firefox_options)
    
    driver.implicitly_wait(10)  # неявные ожидания
    driver.get("https://stellarburgers.nomoreparties.site/")
    
    yield driver
    driver.quit()