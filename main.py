class Article():
   def __init__(self, id, author_id, title, content, date, likes):
      self.id = id
      self.author_id = author_id
      self.title = title
      self.content = content
      self.date = date
      self.likes = likes

   def new_likes(self, number_of_likes):
      if number_of_likes >= 0:
         self.likes = number_of_likes