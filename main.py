class Article:
   def __init__(self, id, author_id, title, content, date, likes):
      self.id = id
      self.author_id = author_id
      self.title = title
      self.content = content
      self.date = date
      self.likes = likes

   def __str__(self):
        return f"Article:\nid - {self.id}\nauthor_id - {self.author_id}\ntitle - {self.title}\ncontent - {self.content}\ndate - {self.date}\nlikes - {self.likes}"

   def  ChangeLikes(self):
      new_values = int(input("Введіть нове значення для к-сті лайків: "))
      self.likes = new_values 

article1 = Article(1091, 1102, 'Штучний інтелект', 'Штучний інтелект революціонізує спосіб, яким ми взаємодіємо з технологіями, відкриваючи нові можливості для наукових досліджень та повсякденного життя.', '23-10-2023', 250)

print(article1)
print()
print('Застосування методу')
print()

article1.ChangeLikes()

print()
print(article1)