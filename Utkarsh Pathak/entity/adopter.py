# entity/model/adopter.py
from dao.Iadoptable import IAdoptable

class Adopter(IAdoptable):
    def adopt(self):
        print("Adopter: Adopting a pet from the shelter.")
