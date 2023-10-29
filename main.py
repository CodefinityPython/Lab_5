class Article:
    def __init__(self, id, author_id, title, content, date, likes):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.content = content
        self.date = date
        self.likes = likes

    # Метод для зміни кількості лайків
    def update_likes(self, new_likes):
        self.likes = new_likes

# Приклад створення об'єкту Article
article = Article(1, 123, "Sample Title", "Sample Content", "2023-10-29", 10)

# Приклад виклику методу для зміни кількості лайків
print(f"Початкова кількість лайків: {article.likes}")
article.update_likes(15)
print(f"Нова кількість лайків: {article.likes}")