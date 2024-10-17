from entity.donation import Donation
from datetime import datetime

class CashDonation(Donation):
    def __init__(self, donorName, amount, donationDate: datetime):
        super().__init__(donorName, amount)
        self.donationDate = donationDate

    def recordDonation(self):
        print(f"Recording cash donation: {self.donorName} donated ${self.amount:.2f} on {self.donationDate.strftime('%Y-%m-%d')}.")

