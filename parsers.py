from abc import ABC, abstractmethod
from typing import override

"""
An parser takes in a string represented in the format of a language
and operations, and evaluates the expression according to rules defined in 
the parser.
"""
class ExpressionParser(ABC):
    @abstractmethod
    def parse(expression: str) -> str:
        pass

class DefaultExpressionParser(ExpressionParser):
    def __init__(self, rules: list[Rule]):
        self.language = DefaultLanguage()
        self.rules = rules

    def __init__(self, language: Language, rules: list[Rule]) -> None:
        self.language = language 
        self.rules = rules 
    
    @override
    def parse(expression: str) -> str:
        return None
