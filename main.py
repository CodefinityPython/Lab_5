class Article:
    def __init__(self, id, author_id, title, content, date, likes):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.content = content
        self.date = date
        self.likes = likes


# створення методу
    def plus_likes(self):
        self.likes = self.likes + 1

Article = Article(1, 2,44,44, 17.10, 11)

print("до", Article.likes)

Article.plus_likes()
print("після", Article.likes)







