class Comment():
    def __init__(self, id, author, content, date):
        self.id = id
        self.author = author
        self.content = content
        self.date = date
 # створення методу
    def editing(self, new_text):
        self.content = new_text

new_content = Comment( 178, 'Sasha', 'sports is the life', '21.10.2023')
print('Це був наш старий контент:', new_content.content)
new_content.editing('no pain no gain')
print('Це новий контент:', new_content.content)
