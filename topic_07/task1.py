class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} - {self.author} ({self.pages} стор.)"

    def __repr__(self):
        return f"{self.title}, {self.author}, {self.pages} стор."

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages

    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("Кобзар", "Тарас Шевченко", 320)
book2 = Book("Захар Беркут", "Іван Франко", 240)
book3 = Book("Кобзар", "Тарас Шевченко", 320)

print(book1)

print([book1, book2])

print("book1 == book3:", book1 == book3) 
print("book1 == book2:", book1 == book2)

print("book2 < book1:", book2 < book1)
print("Відсортовані:", sorted([book1, book2]))

print("Разом сторінок:", book1 + book2)