from abc import ABC,abstractmethod

class Donation(ABC):
    def __init__(self, donorName: str, amount: float):
        self.donorName = donorName
        self.amount = amount

    @abstractmethod
    def recordDonation(self):
        pass