from abc import ABC, abstractmethod

"""
An operation represents the simplest execution that can occur
within an expression. Operations can operate across multiple
characters in a language and can be represented in multiple ways.

"""
class Operation(ABC):

    @abstractmethod
    def execute(self, *operands: list[str]) -> str:
