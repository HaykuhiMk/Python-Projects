from typing import Any

class Cell:
    def __init__(self, value: int):
        self.value = value
        self.founded : bool = False

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value: Any):
        self.__value = value

    @property
    def founded(self):
        return self.__founded
    
    @founded.setter
    def founded(self, founded: bool):
        if not isinstance(founded, bool):
            raise TypeError("Invalid type!")
        self.__founded = founded

    def __eq__(self, other: "Cell"):
        if not isinstance(other, Cell):
            raise TypeError("Invalid type!")
        return self.value == other.value
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
