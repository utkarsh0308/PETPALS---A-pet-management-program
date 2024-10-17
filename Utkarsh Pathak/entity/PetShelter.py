from entity.pet import Pet
from exceptions import nullReferenceException

class PetShelter:
    def __init__(self):
        self.availablePets = []

    def addPet(self,pet:Pet):
        self.availablePets.append(pet)

    def removePet(self,pet:Pet):
        if pet in self.availablePets:
            self.availablePets.remove(pet)
        else:
            print("Pet not found!")

    def listAvailablePets(self):
        if not self.availablePets:
            print("No pets foound for adoption!")
        else:
            for pet in self.availablePets:
                try:
                    if pet.name is None or pet.age is None or pet.breed is None:
                        raise nullReferenceException("Pet has missing information")
                    print(pet)
                except nullReferenceException as e:
                    print(f"Error: {e}")
                