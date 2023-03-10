import csv
import random


class Animal:
    def __init__(self, name: str, numLegs: int, sound: str):
        self.name = name
        self.numLegs = int(numLegs)
        self.sound = sound

    def __repr__(self):
        return f"{self.name}: {self.numLegs} \"{self.sound}\""


class Monster:
    def __init__(self, head: Animal, body: Animal):
        assert head.numLegs == body.numLegs
        self.name = head.name + body.name
        self.sound = head.sound + body.sound
        self.numLegs = head.numLegs

    def __repr__(self):
        return f"{self.name}: {self.numLegs} \"{self.sound}\""


def createAllMonsters(num_legs):
    possible_animals = [animal for animal in all_animals if animal.numLegs == num_legs]
    monsters = []
    for i, head in enumerate(possible_animals):
        for body in possible_animals[i+1:]:
            monsters.append(Monster(head, body))
    return monsters


def getRandomMonster(num_legs):
    return random.choice(createAllMonsters(num_legs))


all_animals_dicts = csv.DictReader(open('animals.txt'))
all_animals = [Animal(animal['AnimalName'], animal['NumLegs'], animal['Sound']) for animal in all_animals_dicts]
print(all_animals)
print(createAllMonsters(4))
print(getRandomMonster(4))
