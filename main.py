class User:
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password
    def change_password(self, new_password):
        self.password = new_password


class Comment:
     def __init__(self, id, author, content, date):
         self.id = id
         self.author = author
         self.content = content
         self.date = date
     def edit_content(self, new_content):
         self.content = new_content
class Article:
    def __init__(self, id, author_id, title, content, date, likes):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.content = content
        self.date = date
        self.likes = likes

    def change_likes(self, new_likes):
        self.likes = new_likes

