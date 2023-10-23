class User:
   def __init__(self, id, name, user_name, password):
      self.id = id
      self.name = name
      self.user_name = user_name
      self.password = password

   def change_password(self, new_password):
        self.password = new_password


# Створення об'єкта користувача
user1 = User(1, "Maria", "Mariyaa", "12345678masha")

 # Зміна паролю
user1.change_password("12345678masha")

# Ввести новий пароль
print(f"User 1: {user1.name}, Username: {user1.user_name}, Password: {user1.password}")


# Створення об'єкта користувача
user2 = User(2, "Nikita", "Nikita2020", "12345NiKiTa")

# Зміна паролю
user2.change_password("12345NiKiTa")

# Ввести новий пароль
print(f"User 2: {user2.name}, Username: {user2.user_name}, Password: {user2.password}")


