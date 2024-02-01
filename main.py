import random
#Библиотеки
class Crocodile:
    def __init__(self, name):
        self.hunger = 0
        self.sat = 0
        self.name = name
        self.glad = 0
        self.toilet = 0
        self.owner = False
        self.activity = 0
        self.sleep = 0
        self.alive = True

    def to_owner(self):
        print("Нашёл хозяина")
        self.owner = True
        self.glad += 10

    def to_eat(self):
        print("Пора есть")
        self.sat += 14
        self.hunger -= 12
        self.toilet += 1

    def to_walk(self):
        self.activity += 5
        self.hunger += 10
        self.sat -= 10
        self.sleep += 1

    def to_sleep(self):
        self.sleep = 0
        self.glad += 5
        self.sat -= 5
        self.toilet += 3

    def is_alive(self):
        if self.glad > 5:
            self.alive = True

    def to_toilet(self):
        self.toilet -= 1
        self.glad += 2
        self.sat -= 5
        self.hunger += 3
    def hungry(self):
        if self.hunger < 7:
            print("Вы сожрали хозяина")
            self.owner = False
        elif self.glad < 0:
            print("Вы сьели хозяина")
            self.owner = False
        elif self.hunger < 10:
            self.alive = False
    def no_activity(self):
        print("Лень")
        self.activity -= 5
        self.glad += 5
        self.sleep += 2

    def end_of_the_day(self):
        self.sleep += 5
        self.hunger += 4
    def no_toilet(self):
        if self.toilet < 5:
            self.toilet = 0
            print("В Тапки")
    def to_bed(self):
        if sleep > 5:
            self.sleep = 0
            print("Вы уснули")
    def live(self, day):
        d = f"Day{day} of {self.name} live"
        print(f"{d:=^50}")
        live_cube = random.randint(1, 6)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.no_activity()
        elif live_cube == 4:
            self.to_toilet()
        elif live_cube == 5:
            self.no_toilet()
        elif live_cube == 6:
            self.to_walk()
        self.end_of_the_day()
        self.is_alive()
toothless = Crocodile("Toothless")
for day in range(1, 366):
    if toothless.is_alive == False:
        break
    toothless.live(day)