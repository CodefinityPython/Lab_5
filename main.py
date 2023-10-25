class User:
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password
    
    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            return True
        else:
            return False

user1 = User(1, "Artur", "artur_bosuj", "1233")

old_password = input('Enter your current password: ')
new_password = input('Enter your new password: ')

if user1.change_password(old_password, new_password):
    print('Congratulations, your password has been changed.')
    print('Updated password:', user1.password)
else:
    print('The password entered is incorrect.')
