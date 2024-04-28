from typing import List

from battleshipValidator import CompositeValidator, ShipFieldValidator, ShipFormValidator, ShipsNumberValidator, \
    ShipsIntersectionsValidator


def validate_battlefield(field: List[List[int]]):
    return CompositeValidator().add_primitive(ShipFieldValidator(field)).add_primitive(
        ShipFormValidator(field)).add_primitive(ShipsNumberValidator(field)).add_primitive(
        ShipsIntersectionsValidator(field)).validate()


if __name__ == '__main__':
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    result = validate_battlefield(battleField)
    print(result)
