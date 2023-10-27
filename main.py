class User:
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password

    def change_password(self, new_password):
        self.password = new_password
        print("Успішна зміна паролю!")


user = User(1, "Matvey Klob", "matveyklb", "mat123123")
print(user.password)

user.change_password("mat12341234")
print(user.password)
