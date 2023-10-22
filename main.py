class User:
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.id = user_name
        self.password = password
    
    def changePassword(self, newPassword):
        self.password = newPassword

newUser = User(id="1", name="Artur",user_name="artur_levchuk", password="1234")
print(f"Old password: {newUser.password}")
newUser.changePassword("9999")
print(f"New password: {newUser.password}")