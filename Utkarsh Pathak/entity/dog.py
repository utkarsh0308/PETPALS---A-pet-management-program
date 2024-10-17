from entity.pet import Pet

class Dog(Pet):
    def __init__(self, name: str, age: int, breed: str, dogBreed: str):
        super().__init__(name, age, breed)
        self.dogBreed = dogBreed

    def get_dogBreed(self):
        return self.dogBreed
    
    def set_dogBreed(self, dogBreed: str):
        self.dogBreed = dogBreed