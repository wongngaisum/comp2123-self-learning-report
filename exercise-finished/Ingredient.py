#!/usr/bin/python
from abc import *
import random

class Ingredient(ABC):
    def __init__(self, min, max):
        super().__init__()
        self.volume = random.randint(min, max)

    def getVolume(self):
        return self.volume

    @abstractmethod
    def getName(self):
        pass

class IngredientCreator(ABC):
    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def createIngredient(self):
        pass

    @abstractmethod
    def getName(self):
        pass
