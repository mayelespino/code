#!/usr/local/bin/python3
#
# This is based, almost with out change, on the example in the lynda.com "Python 3 essencial training"
# by: Bill Weinman.
#

class AnimalActions:
    def quack(self): return self._doAction('quack')
    def feathers(self): return self._doAction('feathers')
    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')
    def _doAction(self,action):
        if action in self.strings:
            return self.strings[action]
        else:
            return "{} can not perform {} action.".format(__class__.__name__,action)

class Duck(AnimalActions):
    strings = dict(
        quack = "Duck does quack.",
        feathers = "Duck has feathers.",
        bark = "Duck does not bark.",
        fur ="Duck has no fur."
    )

class Person(AnimalActions):
    strings = dict(
        quack = "Person can immitate quack.",
        feathers = "Person has not feathers.",
        bark = "Person can immitate bark.",
        fur ="Person can put on fur."
    )

class Dog(AnimalActions):
    strings = dict(
        quack = "Dog can not quack.",
        feathers = "Dog has not feathers.",
        bark = "Dog does bark.",
        fur ="Dog has fur."
    )

def in_the_forest(duck):
    print("\n\nIn the forest:")
    print(duck.feathers())
    print(duck.quack())

def in_the_house(person):
    print("\n\nIn the house:")
    print(person.bark())
    print(person.quack())
    print(person.fur())
    print(person.feathers())

def in_the_doghouse(dog):
    print("\n\nIn the dog house:")
    print(dog.fur())
    print(dog.bark())

def main():
    Dunald = Duck()
    John = Person()
    Fido = Dog()
    for o in (Dunald, John, Fido):
        in_the_forest(o)
        in_the_doghouse(o)
        in_the_house(o)

if __name__ == "__main__" : main()