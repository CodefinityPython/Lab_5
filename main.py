# Варіант 1
# Створіть class User

# Створіть властивості

# id
# name
# user_name
# password
# Cтворіть метод для зміни паролю

class User:
    id = ""
    name  = ""
    user_name = ""
    password = ""
    
    def __init__(self, user_data):
        self.id = user_data["id"]
        self.name = user_data["name"]
        self.user_name = user_data["user_name"]
        self.password = user_data["password"]
    
    def change_password(self, password):
        self.password = password

    def print_user_data(self):
        print(f"User: {self.user_name}, Password: {self.password}")


dict_user_data = {"id": 1, "name": "John", "user_name": "RealHuman", "password": "realhuman"}

user_1 = User(dict_user_data)
user_1.print_user_data()

new_password = input(f"Please enter new password for {user_1.user_name}: ")
user_1.change_password(new_password)
user_1.print_user_data()