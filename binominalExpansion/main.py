from expressionParser import ExpressionParser


def differentiate(equation: str, point: float):
    expression = ExpressionParser.parse_polynomial(equation)
    return expression.differentiate().compute(point)


if __name__ == '__main__':
    equation = "x^2-x"
    point = 3
    result = differentiate(equation, point)
    print(result)

