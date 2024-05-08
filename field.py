class Field:
    def __init__(self, value: str) -> None:
        self.set_value(value)

    def __str__(self) -> str:
        return str(self._value)
    
    def get_value(self) -> str:
        return self._value
    
    def set_value(self, value: str) -> None:
        self._value = value