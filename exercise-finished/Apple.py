#!/usr/bin/python
from Ingredient import *

class Apple(Ingredient):
    def __init__(self):
        super().__init__(50, 100)

    def getName(self):
        return "Apple"

class AppleCreator(IngredientCreator):
    def __init__(self):
        super().__init__()

    def createIngredient(self):
        return Apple()

    def getName(self):
        return "Apple"
