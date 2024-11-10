from random import randint

class RandomValues:
    name = f'Praktik{randint(100, 999)}'
    email = f'Praktikum{randint(100, 999)}@ya.ru'
    password = f'Prak{randint(100, 999)}'


class Url:
    main_page = 'https://stellarburgers.nomoreparties.site' # главная страница
    login_page = f'{main_page}/login' # страница входа в личный кабинет
    register_page = f'{main_page}/register' # страница регистрации
    forgot_password = f'{main_page}/forgot-password' # страница восстановления пароля

