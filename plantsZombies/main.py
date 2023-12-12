from typing import Optional

from model import Simulation
from my_very_unique_project_types import LawnRawT, ZombieStatsRawT


def plants_and_zombies(lawn_raw: LawnRawT, zombies_raw: ZombieStatsRawT) -> Optional[int]:
    simulation = Simulation(lawn_raw, zombies_raw)
    simulation.simulate()
    return simulation.simulation_result()


if __name__ == '__main__':
    lawn = [
        '2       ',
        '  S     ',
        '21  S   ',
        '13      ',
        '2 3     '
    ]
    zombies = [[0, 4, 28], [1, 1, 6], [2, 0, 10], [2, 4, 15], [3, 2, 16], [3, 3, 13]]
    print(plants_and_zombies(lawn, zombies))
