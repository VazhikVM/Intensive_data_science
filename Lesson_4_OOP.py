class User:
    count = 0
    __password = 'qwerty'

    def __init__(self, name, login):
        self.name = name
        self.__login = login

        User.count += 1

    def show_info(self):
        print(self.name, '\t', self.__login)

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        raise Exception("You can not see this password")

    @password.setter
    def password(self, value):
        # print("Внимание, пароль должен содержать не менее 3 символов и один из знаков _, %, #!")
        if len(value) > 3 and \
                (value.__contains__('_') or value.__contains__('%') or value.__contains__('#')):
            self.__password = value
            print('Password changed successfully')
        else:
            print(" Не выполнено условие - пароль должен содержать не менее 3 символов и один из знаков _, %, #!")

    def __repr__(self):
        return f'Пользователь: {self.name}\nЛогин: {self.login}'


class SuperUser(User):
    superuser_count = 0

    def __init__(self, name, login, role):
        super().__init__(name, login)
        self.__role = role

        SuperUser.superuser_count += 1

    def show_info(self):
        print(super().show_info(), self.role)

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        if value:
            self.__role = value
            print(f'New role {value}')
        else:
            print('Не введено значение')

    def __repr__(self):
        return f'Пользователь: {self.name}\nЛогин: {self.login}\nРоль: {self.role}'


user_1 = User('Василий', 'vvasiliy')
user_2 = User('Ivan', 'iiiiivan')

superuser_1 = SuperUser(name='Настя', login='inastya', role='SuperUser')
superuser_2 = SuperUser(name='Максим', login='imax', role='SuperUser')

print(user_1)
print(superuser_2)
print(superuser_2.password)
