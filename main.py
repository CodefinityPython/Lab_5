class Article:
     def __init__(self, id, author_id, title, content, date, likes):
       self.id = id
       self.author_id = author_id
       self.title = title
       self.content = content
       self.date = date
       self.likes = likes

     def new_likes(self, change):
      self.likes = change

new_article = Article(1, 1, 'News', 'Latest info', '22.10.2023', 10)
new_article.new_likes(50)
print(new_article.likes)



