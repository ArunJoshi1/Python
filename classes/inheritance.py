class Animal:
    def walk(self):
        print(f'walk')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


cat=Cat()
cat.walk()