""" Обьектно ориентированное программирование """
""" Наследование и множественное наследование """

# class Game:

#     def __init__(self, game_name, graphics, game_year, company):
#         self.game_name = game_name
#         self.graphics = graphics
#         self.game_year = game_year
#         self.company = company

#     def info(self):
#         print(f'Название игры - {self.game_name}, Максимальная графика {self.graphics},Дата релиза - {self.game_year}, - Создатели - {self.company}')

# game = Game('CsGo', 'Full HD 4K', 2013, 'Valve')
# # game.info()

# class Roblox(Game):

#     def __init__(self, game_name, graphics, game_year, company, multiplayer):
#         super().__init__(game_name, graphics, game_year, company)
#         # Game.__init__(game_name, graphics, game_year, company)
#         self.multiplayer = multiplayer
#         self.name = 'player'
#         self.gender = 'man'
#         self.skin = 'VIP'
#         self.hp = 100

#     # def info(self):
#         # self.multiplayer = multiplayer, Дата релиза - {self.game_year}, - Создатели - {self.company}')
        
#     def info_player(self):
#         print(f'Игрок - {self.name}, Пол - {self.gender}, Облик - {self.skin}, Здоровье - {self.hp}')
#         print('=====================\nROBLOX - Запустился и готов к игре!')

#     def edit_player(self):
#         name = input('Введите имя игрока: ')
#         gender = input('Введите пол игрока: ')
#         skin = input('Введите облик персонажа: ')
#         self.name = name
#         self.gender = gender
#         self.skin = skin

# roblox = Roblox('ROBLOX', 'ULTRA', '2006', 'Roblox corporation', 'да')
# # roblox.info()
# # roblox.edit_player()
# # roblox.info_player()

# class Snake(Roblox):
#     def __init__(self, name, gender, skin):
#         self.name = name
#         self.gender = gender
#         self.skin = skin 
#         self.hp = 100

# snake = Snake('Бека', 'Муж', 'Platinum')

# snake.info_player()



class Animal:

    def __init__(self, name,):
        self.name = name

    def eat(self):
        print(f'{self.name} - ест')

    def sleep(self):
        print(f'{self.name} - спит')
    
lev = Animal('Лев')
lev.eat()
lev.sleep()

class Walker(Animal):
    def __init__(self, name,):
        super().__init__(name)

    def walk(self):
        print(f'{self.name} - ходит')
        
walker = Walker('Лиса')
walker.walk()

class Swimer(Walker):
    def __init__(self, name,):
        super().__init__(name)

    def swim(self):
        print(f'{self.name} - Плавает')
        
walker = Swimer('Волк')
walker.swim()

class Flyer(Swimer):
    def __init__(self, name,):
        super().__init__(name)

    def fly(self):
        print(f'{self.name} - Летает')
        
walker = Flyer('Птица')
walker.fly()

class Penguin (Flyer):

    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f'{self.name}')

pini = Penguin('Пингвин')
pini.describe()

