class User():
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

    print(f"Пароль для користувача {self.user_name} було змінено.")