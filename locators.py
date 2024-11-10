from selenium.webdriver.common.by import By

class Locators:
# Главная страница
    button_set_order = (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка "Оформить заказ"
    button_personal_account = (By.XPATH, "//a[.= 'Личный Кабинет']")  # кнопка "Личный кабинет"
    button_logo_sb = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # кнопка логотипа Stellar Burger
    buns_section = (By.XPATH, "//span[text()='Булки']") # переход в раздел "Булки" в меню конструктора
    sauces_section = (By.XPATH, "//span[text()='Соусы']") # переход в раздел "Соусы" в меню конструктора
    toppings_section = (By.XPATH, "//span[text()='Начинки']") # переход в раздел "Начинки" в меню конструктора
    check_section = (By.XPATH, ".//div[contains(@class, 'current')]/span") # проверка выбранного раздела в конструкторе

# Страница "Регистрация"
    input_name_registration = (By.XPATH, './/label[text()="Имя"]/following-sibling::input') # поле "Имя"
    input_email_registration = (By.XPATH, './/label[text()="Email"]/following-sibling::input') # поле "Email"
    input_password_registration = (By.XPATH, "//input[@name= 'Пароль']") # поле "Пароль"
    button_signup_registration = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка "Зарегистрироваться"
    massage_error_password = (By.XPATH, "//p[text() = 'Некорректный пароль']") # сообщение об ошибке в пароле

# Авторизация
    button_login_authorization = (By.XPATH, "//button[.= 'Войти в аккаунт']")  # кнопка "Войтив аккаунт"
    input_email_authorization =  (By.NAME, "name") # поле "Email"
    input_password_authorization = (By.NAME, "Пароль") # поле "Пароль"
    button_login = (By.XPATH, "//button[text() = 'Войти']")  # кнопка "Войти"


# Личный кабинет
    button_constructor = (By.XPATH, "//p[text()='Конструктор']") # кнопка "Конструктор" в личном кабинете залогиненого пользователя
    button_logout = (By.XPATH, "//button[text()='Выход']") # кнопка "Выход" в личном кабинете залогиненого пользователя


# Восстановление пароля
    button_login_recovery_form = (By.CLASS_NAME, "Auth_link__1fOlj") # кнопка "Войти" в форме Восстановление пароля