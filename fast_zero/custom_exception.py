# Exception personalizada
class BadLanguageException(Exception):
    def __init__(self, name: str):
        self.name = name