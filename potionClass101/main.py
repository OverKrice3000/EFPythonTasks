import math
from typing import Tuple


class Potion:
    color: Tuple[int, int, int]
    volume: int

    def __init__(self, color: Tuple[int, int, int], volume: int):
        self.color = color
        self.volume = volume
        pass

    def mix(self, other: 'Potion'):
        total_volume = self.volume + other.volume
        new_color = (math.ceil((self.color[0] * self.volume + other.color[0] * other.volume) / total_volume),
                     math.ceil((self.color[1] * self.volume + other.color[1] * other.volume) / total_volume),
                     math.ceil((self.color[2] * self.volume + other.color[2] * other.volume) / total_volume))
        return Potion(new_color, total_volume)

potions = [
    Potion((153, 210, 199), 32),
    Potion((135, 34, 0), 17),
    Potion((18, 19, 20), 25),
    Potion((174, 211, 13), 4),
    Potion((255, 23, 148), 19),
    Potion((51, 102, 51), 6)
]
a = potions[0].mix(potions[1])

if __name__ == '__main__':
    print(a.volume)
    print(a.color)
