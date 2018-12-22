#!/usr/bin/python
from Ingredient import *

class Orange(Ingredient):
    def __init__(self):
        super().__init__(150, 200)

    def getName(self):
        return "Orange"

class OrangeCreator(IngredientCreator):
    def __init__(self):
        super().__init__()

    def createIngredient(self):
        return Orange()

    def getName(self):
        return "Orange"
