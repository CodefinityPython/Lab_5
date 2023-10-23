class User():
    def __init__ (self,id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password


    def change_password(self,old_pass, new_pass):
        if self.password == old_pass:
           self.password = new_pass 
           print('parol zmineno')
        else:
            print("parol not valid")   

user1 = User(5050, 'viktor', 'viktor12', 1234)

user1.change_password(1234,4321)