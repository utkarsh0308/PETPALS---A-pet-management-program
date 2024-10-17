class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient donation amount. Minimum is $10."):
        self.message = message
        super().__init__(self.message)
