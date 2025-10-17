from selenium.webdriver.common.by import By

class OrderFeedLocators:
    """Локаторы для ленты заказов."""
    
    # Лента заказов
    ORDER_FEED_SECTION = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Основной контейнер с заказами
    ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__OLh59')]")
    
    # Конкретные заказы - используем ссылки внутри списка
    ORDER_LINKS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__OLh59')]//a[contains(@class, 'OrderHistory_link__1iNby')]")
    FIRST_ORDER_LINK = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_list__OLh59')]//a[contains(@class, 'OrderHistory_link__1iNby')])[1]")
    
    # Альтернативные локаторы
    ORDER_CARDS = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r')]")
    FIRST_ORDER_CARD = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__2x95r')])[1]")
    
    # Номера заказов
    ORDER_NUMBERS = (By.XPATH, "//p[contains(@class, 'text_type_digits-default') and contains(text(), '#')]")
    FIRST_ORDER_NUMBER = (By.XPATH, "(//p[contains(@class, 'text_type_digits-default') and contains(text(), '#')])[1]")
    
    # Модальное окно деталей заказа
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    
    # Счётчики заказов
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    # Кнопка закрытия модального окна
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")