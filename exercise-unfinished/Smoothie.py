#!/usr/bin/python
from Milk import *
from Orange import *
from Apple import *
from Ingredient import *

class Smoothie:
    totalAmount = 0
    ingredients = []

    def __init__(self):
        pass

    def addIngredient(self, newIngred):
        self.ingredients.append(newIngred)
        print("Added " + {name} + " " + {volume} + "ml")
        self.totalAmount = self.totalAmount + {volume}

    def printInfo(self):
        print("Smoothie ingredients: ")
        for i in range(len(self.ingredients)):
            print({name}+ " (" + {volume} + "ml)")
