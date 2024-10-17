class NullReferenceException(Exception):
    def __init__(self, message = "Pet information missing"):
        self.message = message
        super().__init__(self.message)