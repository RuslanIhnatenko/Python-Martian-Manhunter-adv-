class Animal:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def about_me(self):
        print(f"Hello , I am {self.name}, and I am {self.age} years")


class Human(Animal):
    def __init__(self, age, name, weight):
        self.age = age
        self.name = name
        self.wieght = weight

    def eat(self):
        print("I'm very hungry!")

    def sleep(self):
        print("Time to go to sleep")

    def study(self):
        print("I have a new Homework in Cursor,time to do it")

    def work(self):
        print("Just tell me what to do")


class Centaur(Human, Animal):

    def say(self):
        print("Wow, What's wrong with me?")

    def work(self):
        print("Just tell me what to do")


human = Human(43, "Rob", 75)
centaur = Centaur(20, "Nik", 120)
centaur.about_me()
human.about_me()
centaur.say()
