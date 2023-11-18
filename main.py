class User:
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password
        
    def change_password(self, new_password):
        self.password = new_password

user = User(id=1, name = "Your Name", user_name = "your name", password = "qwerty")
print(f"Старий пароль: {user.password}")

new = input("Введіть новий пароль:")

user.change_password(new)
print(f"Ваш новий пароль: {user.password}")