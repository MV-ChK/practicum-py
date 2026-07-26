from typing import Optional


class User:
    def __init__(
            self,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            username: Optional[str] = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Опишите метод класса with_name.
    @classmethod
    def with_name(
		    self,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None
    ):
        return User(first_name, last_name)

    # Опишите метод класса with_username.
    @classmethod
    def with_username(
            self,
		    username: Optional[str] = None
    ):
        if not User.is_username_allowed(username):
            raise ValueError('Некорректное имя пользователя')
        else: 
            return User(None, None, username)

    # Опишите статический метод класса is_username_allowed.
    @staticmethod
    def is_username_allowed(username: str):
        if username.startswith('admin'):
            return False
        else: 
            return True

    # Опишите метод-свойство full_name.
    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        if self.username:
            return '@' + self.username


stas = User.with_name('Стас', 'Басов')
print(stas.full_name)
mir = User.with_username('Chnof')
print(mir.full_name)

# Попробуем создать пользователя с "запрещённым" именем.
# ne_stas = User.with_username('admin_nestas_anonymous')