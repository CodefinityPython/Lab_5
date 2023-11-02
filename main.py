class Comment:
    def __init__(self, id, author, content, date):
        self.id = id
        self.author = author
        self.content = content
        self.date = date

    def edit_content(self, new_content):
        self.content = new_content