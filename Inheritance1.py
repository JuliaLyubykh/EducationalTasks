class Animal:
    def move(self):
        print('Я животное гордое, двигаюсь, как хочу')

    def say_about(self):
        print('Я животное гордое')

class Cat(Animal):
    def move(self):
        print('Я животное вольное, двигаюсь, куда хочу')

    def talk(self):
        print('Мяу-Мяу')


c = Cat()
c.move()
c.talk()
c.say_about()
