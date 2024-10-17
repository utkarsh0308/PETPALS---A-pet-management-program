from entity.donation import Donation

class ItemDonation(Donation):
    def __init__(self, donorName, amount, itemType: str):
        super().__init__(donorName, amount)
        self.itemType = itemType

    def recordDonation(self):
       print(f"Recorded item donation of ${self.amount:.2f} from {self.donorName} for item type: {self.itemType}.")