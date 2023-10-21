class User():
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password
    def change_pass(self, new_password):
        if self.password == old_password:
            self.password = new_password
            return True
        else:
            return False

toha = User(0, 'toha.name', 'toha.user', '123qweab')

old_password = input('Щоб змінити пароль, введіть свій теперіщній пароль: ')
if toha.change_pass(old_password):
    print('Поточний пароль:', toha.password)

# Змінюю пароль
    new_password = input('Придумайте новий пароль: ')
    toha.change_pass(new_password)
    print('Вітаємо, ваш пароль успішно оновлено!')

# Виводжу оновлений пароль
    print('Оновлений пароль:', toha.password)
else:
    print('Введений вами пароль неправильний!')