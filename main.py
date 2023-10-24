class User:
    def __init__(self, user_id, name, user_name, password):
        self.id = user_id
        self.name = name
        self.user_name = user_name
        self.password = password

    def change_password(self, new_password):
        self.password = new_password