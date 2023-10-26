class User:
    def __init__(self, user_id, name, user_name, password):
        self.id = user_id
        self.name = name
        self.user_name = user_name
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

# Створюємо об'єкт user1
user1 = User(1, "John Doe", "john_doe123", "password123")

# Змінюємо пароль
user1.change_password("new_password456")
print(f"New Password: {user1.password}")

