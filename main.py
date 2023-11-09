class User:
    def __init__(self):
        self.name = ""
        self.user_name = ""
        self.password = ""

    def change_password(self, new_password):
        self.password = new_password

# Приклад використання класу User:
user1 = User()
user1.name = "John Doe"
user1.user_name = "johndoe123"
user1.password = "old_password"

print(f"User {user1.name} has the password: {user1.password}")

user1.change_password("new_password")
print(f"User {user1.name}'s password has been changed to: {user1.password}")

