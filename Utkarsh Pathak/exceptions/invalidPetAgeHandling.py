class InvalidPetAgeException(Exception):
    def __init__(self,message="Enter valid age! must be a positive integer"):
        self.message = message
        super().__init__(self.message)