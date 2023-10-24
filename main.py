# Create class Article
class Article:
 # Constructor for class Article
 def __init__ (self, id, author_id, title, content, date, likes):
   self.id = id
   self.author_id = author_id
   self.title = title
   self.content = content
   self.date = date
   self.likes = likes

 # Method for changing likes
 def changing_likes(self, new_likes):
   if new_likes >= 0:
    self.likes = new_likes
   else:
     print("Incorrect value of likes! The value of likes must be positive.")

#--------------------------------------------------------------------------------------------
article1 = Article(1, 101, "Article 1", "Content of an unknown nature 1", "2022-10-24", 10)
article2 = Article(2, 102, "Article 2", "Content of an unknown nature 2", "2023-11-25", 20)

#Example 1 for Article 1
print(f"Initial number of likes for Article 1 = {article1.likes}")

article1.changing_likes(45)

print(f"Changed number of likes for Article 1 = {article1.likes}")

#Enother example for Article 2
print(f"Initial number of likes for Article 2 = {article2.likes}")

article1.changing_likes(-30)

print(f"Changed number of likes for Article 2 = {article2.likes}")

#The value of likes for Article 2 don`t change!
