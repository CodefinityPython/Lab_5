class User:
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password


    def change_user_name(self, new_user_name):
        self.user_name = new_user_name
        print(f"new name: {new_user.user_name}")


    def change_password(self, new_password):
        print(f"password: {new_user.password}")
        self.password = new_password
        print(f"new password: {new_user.password}")


new_user = User(id := 3, name := "Vadym", user_name := "Vadymchek", password := 884567)
print(f"name: {new_user.user_name}")
print('change user name:')
x = input()
new_user.change_user_name(x)
print(f"password: {new_user.password}")
print('change password:')
y = input()
new_user.change_password(y)