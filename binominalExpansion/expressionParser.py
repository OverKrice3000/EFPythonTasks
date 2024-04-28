from expression import Expression, MonomialExpression, PolynomialExpression


class ExpressionParser:
    @staticmethod
    def parse_polynomial(raw_expression: str) -> Expression:
        polynomial = PolynomialExpression()
        for negative_part in raw_expression.split("+"):
            first_positive = negative_part[0] != "-"
            raw_monomials = negative_part.split("-")
            for monomial_index in range(0, len(raw_monomials)):
                if raw_monomials[monomial_index] == "":
                    continue
                if monomial_index == 0 and first_positive:
                    polynomial.add(ExpressionParser.parse_monomial(raw_monomials[monomial_index]))
                else:
                    polynomial.add(ExpressionParser.parse_monomial("-" + raw_monomials[monomial_index]))
        return polynomial

    @staticmethod
    def parse_monomial(raw_expression: str) -> Expression:
        power_index = raw_expression.find("^")
        if power_index == -1:
            raw_base = raw_expression
            raw_power = ""
        else:
            raw_base = raw_expression[:power_index]
            raw_power = raw_expression[power_index + 1:]
        variable = raw_base[len(raw_base) - 1] if raw_base[len(raw_base) - 1].isalpha() else ""
        multiplier = raw_base[:len(raw_base) - 1] if raw_base[len(raw_base) - 1].isalpha() else raw_base
        multiplier = 1 if len(multiplier) == 0 else -1 if multiplier == "-" else multiplier
        power = int(raw_power) if len(raw_power) != 0 else 1 if len(variable) != 0 else 0
        return MonomialExpression(variable, float(multiplier), power)
