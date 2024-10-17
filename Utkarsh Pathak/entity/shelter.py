# entity/model/shelter.py
from dao.Iadoptable import IAdoptable

class Shelter(IAdoptable):
    def adopt(self):
        print("Shelter: Adopting pets to new homes.")
