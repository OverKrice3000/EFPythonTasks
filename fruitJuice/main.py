from typing import Dict


class Jar:
    __amounts_map: Dict[str, int]

    def __init__(self):
        self.__amounts_map = {}

    def add(self, amount, kind):
        current_amount = self.__amounts_map.get(kind)
        current_amount = 0 if current_amount is None else current_amount
        current_amount += amount
        self.__amounts_map[kind] = current_amount

    def pour_out(self, amount):
        total_amount = self.get_total_amount()
        if amount >= total_amount:
            self.__amounts_map = {}
            return

        multiplier = (total_amount - amount) / total_amount
        for i in self.__amounts_map:
            self.__amounts_map[i] *= multiplier

    def get_total_amount(self):
        total_amount = 0
        for i in self.__amounts_map:
            total_amount += self.__amounts_map[i]
        return total_amount

    def get_concentration(self, kind):
        kind_amount = self.__amounts_map.get(kind)
        total_amount = self.get_total_amount()
        return 0 if kind_amount is None else kind_amount / total_amount


if __name__ == '__main__':
    pass
