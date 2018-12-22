#!/usr/bin/python
from Smoothie import *
from Milk import *
from Orange import *
from Apple import *
from Ingredient import *

class Shop:
    ingredients = ???
    smoothie = ???

    def __init__(self):
        pass

    def askForIngredients(self):
        while True:
            for i in range(len(self.ingredients)):
                print(str(i + 1) + '.' + self.ingredients[i].getName())

            print("What would you like to add to your smoothie?")

            try:
                choice = int(input("Please enter your choice (1-" + str(len(self.ingredients)) + ", or 0 to finish the order): "))

                if choice == 0:
                    break
                elif choice > 0 and choice < len(self.ingredients) + 1:
                    ingredient = self.ingredients[choice - 1].createIngredient()
                    self.smoothie.???
            except:
                print("Error occured.")

    def start(self):
        self.askForIngredients()
        self.smoothie.printInfo()

Shop().start()
