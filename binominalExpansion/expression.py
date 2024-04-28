from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional


class Expression(ABC):
    @abstractmethod
    def differentiate(self) -> Expression:
        pass

    @abstractmethod
    def add(self, multiplier) -> Expression:
        pass

    @abstractmethod
    def compute(self, point: float) -> float:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass


class MonomialExpression(Expression):
    __variable: str
    __multiplier: float
    __power: int

    def __init__(self, variable: str, multiplier: float, power: int):
        self.__variable = variable
        self.__multiplier = multiplier
        self.__power = power

    def add(self, expression: Expression) -> Expression:
        if isinstance(expression, MonomialExpression) and expression.__power == self.__power:
            return MonomialExpression(self.__variable, self.__multiplier + expression.__multiplier, self.__power)
        else:
            return PolynomialExpression(self).add(expression)

    def compute(self, point: float) -> float:
        return self.__multiplier * pow(point, self.__power)

    def differentiate(self) -> Expression:
        return MonomialExpression(self.__variable, self.__multiplier * self.__power, 0 if self.__power == 0 else self.__power - 1)

    def to_string(self) -> str:
        if self.__power == 0:
            return self.__multiplier.__str__()
        elif self.__power == 1:
            self.__multiplier.__str__() + self.__variable
        return self.__multiplier.__str__() + self.__variable + "^" + self.__power.__str__()


class PolynomialExpression(Expression):
    __monomials: List[Expression]

    def __init__(self, expression: Optional[Expression] = None):
        self.__monomials = [] if expression is None else [expression]

    def add(self, expression: Expression) -> Expression:
        self.__monomials.append(expression)
        return self

    def compute(self, point: float) -> float:
        result = 0
        for monomial in self.__monomials:
            result += monomial.compute(point)
        return result

    def differentiate(self) -> Expression:
        target_polynomial = PolynomialExpression()
        for monomial in self.__monomials:
            target_polynomial.add(monomial.differentiate())
        return target_polynomial

    def to_string(self) -> str:
        target_str = ""
        for monomial in self.__monomials:
            monomial_str = monomial.to_string()
            if monomial_str == "0":
                continue
            if len(target_str) != 0 and len(monomial_str) != 0 and monomial_str[0] != "-":
                target_str += "+" + monomial_str
            else:
                target_str += monomial_str
        return target_str
