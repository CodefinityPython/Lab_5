x = input('Enter new password :')
class User():
    def __init__(self, name, user_name, password):
        self.name = name
        self.user_name = user_name
        self.password = password
    def password_change(self):
     self.password = x

user17 = User(name='Taras', user_name= 'Slave_of_Jesus', password= '190455')

print('Old', user17.password)
user17.password_change()
print("New", user17.password)
