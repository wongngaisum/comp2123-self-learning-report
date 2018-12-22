#!/usr/bin/python
from Ingredient import *

class Milk(Ingredient):
    def __init__(self):
        super().__init__(100, 150)

    def getName(self):
        return "Milk"

class MilkCreator(IngredientCreator):
    def __init__(self):
        super().__init__()

    def createIngredient(self):
        return Milk()

    def getName(self):
        return "Milk"
