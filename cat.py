#cat simulation 
import random


class Cat:

    def __init__(self, name, breed, colour):
        self.name = name
        self.breed = breed
        self.colour = colour

    #actions
    def petCat(self):
        print("You pet", self.name)
        self.happyReaction()

    def washCat(self):
        print("You wash", self.name)
        self.sadReaction()

    def feedCat(self):
        print("You feed", self.name)
        self.ignoreReaction()

    def entertainCat(self):
        print("You try to entertain", self.name)
        self.randomReaction()

    #reactions
    def happyReaction(self):
        print(self.name, "is happy")

    def sadReaction(self):
        print(self.name, "is sad")

    def ignoreReaction(self):
        print(self.name, "ignores you")

    def randomReaction(self):
        num = random.randint(0, 2)
        
        if num == 0:
            self.happyReaction()
        elif num == 1:
            self.ignoreReaction()
        elif num == 2:
            self.sadReaction()


def main():
    bob = Cat("Bob", "Maine Coone", ["Black", "white"])

    while True:
        command = input("What do you want to do with the cat? ")
        if command == "wash":
            bob.washCat()
        elif command == "pet":
            bob.petCat()
        elif command == "feed":
            bob.feedCat
        elif command == "entertain":
            bob.entertainCat()
        else:
            print("Command not recognised")
        
    #bob.petCat()
    #bob.washCat()
    #bob.feedCat()
    #bob.entertainCat()
    

main()    
