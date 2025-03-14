
from abc import ABC, abstractmethod
from typing import override

"""
A language represents the simplest element an operator can operate on.
Characters can be any size and shape, and will be parsed according to
the rules provided.
"""
class Language(ABC):
    @abstractmethod
    def characters() -> list[Character]:
        pass 

class DefaultLanguage(Language):
    @override
    def characters():
        return [Character(i) for i in range(1, 11)]

class Character:
    def __init__(self, char: str) -> None:
        self.char = char      