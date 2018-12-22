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
        print("Added " + newIngred.getName() + " " + str(newIngred.getVolume()) + "ml")
        self.totalAmount = self.totalAmount + newIngred.getVolume()

    def printInfo(self):
        print("Smoothie ingredients: ")
        for i in range(len(self.ingredients)):
            print(self.ingredients[i].getName() + " (" + str(self.ingredients[i].getVolume()) + "ml)")
