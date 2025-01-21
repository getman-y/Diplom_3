from random import Random


class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
    FEED_URL = f'{MAIN_URL}feed'
    REGISTER_URL = f'{MAIN_URL}register'
    ACCOUNT_URL = f'{MAIN_URL}account/profile'
    HISTORY_OR_ORDER_URL = f'{MAIN_URL}account/order-history'
    LOGIN_URL = f'{MAIN_URL}login'
    FORGOT_PASSWORD_URL = f'{MAIN_URL}forgot-password'
    RESET_PASSWORD_URL = f'{MAIN_URL}reset-password'


class UserData:
    @staticmethod
    def user_data_for_register():
        random = Random()
        random_number = str(random.randint(1000, 9999))
        email = f'getmanyuliia{random_number}@yandex.ru'
        password = '123456'
        name = f'Юля{random_number}'
        return [name, email, password]