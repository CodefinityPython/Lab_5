from datetime import datetime


class Comment:
    def __init__(self, id, author, content, date):
        self.id = id
        self.author = author
        self.content = content
        self.date = date
    def edit_content(self, new_content):
        self.content = new_content
    def __str__(self) -> str:
        return f"Id: {self.id}, Author: {self.author}, Content: {self.content}, Date: {self.date}"


    

comment1 = Comment("1", "Kiril", "Old content", date=datetime.now())

print(comment1.__str__())

comment1.edit_content("New content")

print(comment1.__str__())