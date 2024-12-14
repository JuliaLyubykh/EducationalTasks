class Animal:
    def move(self):
        print('Я животное гордое')

    def say_about(self):
        print('Я животное гордое')

class Cat(Animal):
    def move(self):
        print('Я животное вольное')

    def talk(self):
        print('Мяу-Мяу')


c = Cat()
c.move()
c.talk()
c.say_about()
