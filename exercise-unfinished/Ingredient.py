#!/usr/bin/python
#???
#???

class Ingredient(ABC):
    def __init__(self, min, max):
        super().__init__()
        self.volume = random.randint(min, max)

    def getVolume(self):
        return self.volume

    #???
    def getName(self):
        pass

class IngredientCreator(ABC):
    def __init__(self):
        super().__init__()
        pass

    #???
    def createIngredient(self):
        pass

    #???
    def getName(self):
        pass
