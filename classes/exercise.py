class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f'hi, iam {self.name}')


arun = Person('arun joshi')
arun.talk()
bob = Person('bob smith')
bob.talk()