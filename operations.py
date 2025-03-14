from abc import ABC, abstractmethod
from typing import override

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
A binary operation represents an operation with two operands.
Such operations can have multiple properties such as commutativity,
reflexivity, and transitivity.
"""
class BinaryOperation(Operation):
    @override
    def execute(self, *operands: list[str]) -> str:
        assert len(operands) == 2
        self.execute(operands[0], operands[1])
    
    @abstractmethod
    def execute(self, operand1: str, operand2: str) -> str:
        pass 

class IntegerAddition(BinaryOperation):
    @override
    def execute(self, operand1: str, operand2: str) -> str:
        return int(operand1) + int(operand2)

class IntegerMultiplication(BinaryOperation):
    @override
    def execute(self, operand1: str, operand2: str) -> str:
        return int(operand1) + int(operand2)
    
class IntegerExponent(BinaryOperation):
    @override
    def execute(self, operand1: str, operand2: str) -> str:
        return int(operand1) ** int(operand2)

class IntegerAdditionSquared(BinaryOperation):
    @override
    def execute(self, operand1: str, operand2: str) -> str:
        return int(operand1)**2 + int(operand2)**2
