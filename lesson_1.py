# """ Обьектно ориентированное программирование """
# # full_name = 'аслан' # змеиний регистр
# # FullName = "Жибек"   # верблюжий регистр

# class Car: # шаблон или же чертёж обьекта
#     def __init__(self,marka,  model, color): # __init__ (магический метод конструктор)
#        # АТРИБУТ обьекта
#         self.marka = marka # self (ссылка на текущий обьект)
#         self.model = model
#         self.color = color
#         #атрибут класса
#         self.bak = 10
#         self.is_start = False
#     def info(self):
#         print(f'марка машины - {self.marka}, модель - {self.model} , цвет - {self.color}')

#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f'машина {self.marka} - {self.model} заведения ')
#         else:
#             print(f'машина {self.marka} - {self.model} нет топлива ')

    # def stop(self):
    #     self.is_start = False
    #     print(f'машина {self.marka} - {self.model} заглушено')

#     def drive(self, city):
#         if self.is_start == True:
#             print(f'машина {self.marka} - {self.model} едет в {city}')
#         else:
#             print(f'машина {self.marka} - {self.model} не заведено')

# bmw = Car('BMW','M5 F90', 'Black')
# bmw.info()
# bmw.start()
# # bmw.stop()
# bmw.drive('Дубай')


class book :
    def __init__(self, avtor, book_name, year):
        self.avtor = avtor # self (ссылка на текущий обьект)
        self.book_name = book_name
        self.year = year

    def info (self):
        print(f'Автор книги - {self.avtor}, имя книги- {self.book_name} , Год книги - {self.year}')

kniga = book('Владимир П.', 'путь в москву', '1888')
kniga.info()