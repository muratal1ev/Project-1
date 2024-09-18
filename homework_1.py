# 1
# class frukt:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def info(self):
#         print(f"Названия фрукты - {self.name}, свет - {self.color}, масса - {self.weight}")    

# apple = frukt('Дыня', 'Желтый', '50гр')
# apple.info()

# 2 

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def check_pages(self):
        if self.pages < 100:
            print(f"Книга '{self.title}' автора {self.author} тонкая.")
        elif 100 <= self.pages <= 300:
            print(f"Книга '{self.title}' автора {self.author} средняя.")
        else:
            print(f"Книга '{self.title}' автора {self.author} толстая.")


book1 = Book("Ак кеме", "Ч.Айтматов", 95)
book2 = Book("Сынган кылыч", "Тологон К.", 250)
book3 = Book("Архат", "Казат А.", 450)

book1.check_pages()  
book2.check_pages() 
book3.check_pages()      
  

 