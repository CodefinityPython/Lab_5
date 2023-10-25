class User():
    id = ''
    name = ''
    user_name = ''
    password = ''
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password

    def change_password(self, current_password, new_password):
        if self.password == current_password:
            self.password == new_password
            print('Successfully password change!')
        else:
            print('Current password is incorrect!')

usr = User(10, 'Alex', 'Anna', '123456')
usr.change_password('123457', '1fet234')
usr.change_password('123456', '1fet234')

