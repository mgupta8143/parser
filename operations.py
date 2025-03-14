from abc import ABC, abstractmethod

"""
An operation represents the simplest execution that can occur
within an expression. Operations can operate across multiple
characters in a language and can be represented in multiple ways.
"""
class Operation(ABC):
    @abstractmethod
    def execute(self, *operands: list[str]) -> str:
        pass 

"""
A binary operation represents the simplest operation, in that
it can only operate on two operands.
"""
class BinaryOperation(Operation):
    def execute(self, *operands: list[str]) -> str:
        assert len(operands) == 2
        self.execute(operands[0], operands[1])
    
    @abstractmethod
    def execute(self, operand1: str, operand2: str) -> str:
        pass 

class Addition(BinaryOperation):

    def execute(self, operand1: str, operand2: str) -> str: