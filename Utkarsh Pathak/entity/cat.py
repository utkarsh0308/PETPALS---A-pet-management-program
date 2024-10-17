from entity.pet import Pet

class Cat(Pet):
    def __init__(self, name: str, age: int, breed: str, catColour: str):
        super().__init__(name, age, breed)
        self.catColour = catColour

    def get_catColour(self):
        return self.catColour
    
    def set_catColour(self, catColour: str):
        self.catColour = catColour
    
