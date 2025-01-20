from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCT_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    FEEDS_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    BUN_SNIPPET = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    MODAL_WIH_DETAILS_INGREDIENTS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CLOSE_MODAL_WIH_DETAILS_INGREDIENTS = By.XPATH, '//button[contains(@class,"close")]'
    TITLE_MAIN_PAGE = By.XPATH, "//h1[text()='Соберите бургер']"
    ORDER_SNIPPET = (By.XPATH, "//span[text()='Перетяните булочку сюда (низ)']")
    INGREDIENTS_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_ID = (By.XPATH, '//p[text()="идентификатор заказа"]')