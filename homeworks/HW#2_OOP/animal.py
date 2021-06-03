class Animal:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def about_me(self):
        print(f"Hello , I am an animal, and I am {self.age} years")


class Raccoon(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def weight_raccoon(self):
        if self.weight > 15:
            print("I am not heavy , it is all fur")
        else:
            print("Racoon is never too much")


class Otter(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def destroy(self):
        print(f"My name is {self.name} and I am very nice otter, and I can destroy all your house)")


class Owl(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def sleep(self):
        print("I really want to sleep ,5 more minutes")


class RedPanda(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def active(self):
        print("I am the most active animal on the planet, you can't stop me")


class Puma(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def big_cat(self):
        print("I am a very big cat,and now this house is mine")


puma = Puma(5, 23, "Messi")
panda = RedPanda(4, 12, "Dasha")
owl = Owl(2, 3, "Sonya")
otter = Otter(6, 8, "Hana")
raccoon = Raccoon(12, 4, "Jack")

for animal in (puma, panda, owl, otter, raccoon):
    animal.about_me()

puma.big_cat()
panda.active()
owl.sleep()
otter.destroy()
raccoon.weight_raccoon()