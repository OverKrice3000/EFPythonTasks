from functools import cmp_to_key
from typing import Optional, List, Union

from my_very_unique_project_types import LawnRawT, ZombieStatsRawT
from utils import sign


class Zombie:
    __current_hp: int
    __move_number: int
    __row: int
    __column: int

    def __init__(self, move_number: int, row: int, hp: int, column: int):
        self.__row = row
        self.__current_hp = hp
        self.__move_number = move_number
        self.__column = column

    def hit(self, damage: int):
        reduced_hp = self.__current_hp - damage
        self.__current_hp = max(0, reduced_hp)
        return abs(min(0, reduced_hp))

    def move_number(self):
        return self.__move_number

    def has_entered_house(self):
        return self.__column < 0

    def is_dead(self):
        return self.__current_hp == 0

    def move(self):
        self.__column -= 1

    def row(self):
        return self.__row

    def column(self):
        return self.__column

    def hp(self):
        return self.__current_hp


class NumberedShooter:
    __strength: int
    __row: int
    __column: int

    def __init__(self, row: int, column: int, strength: int):
        self.__row = row
        self.__column = column
        self.__strength = strength

    def strength(self):
        return self.__strength

    def row(self):
        return self.__row

    def column(self):
        return self.__column


class SShooter:
    __row: int
    __column: int

    def __init__(self, row: int, column: int):
        self.__row = row
        self.__column = column

    def row(self):
        return self.__row

    def column(self):
        return self.__column


Square = Optional[Union['Zombie', 'Shooter']]
Lawn = List[List[Square]]


class Simulation:
    __numbered_shooters: List[List['NumberedShooter']]
    __sshooters: List['SShooter']

    __zombies_pending: List['Zombie']
    __zombies_active: List['Zombie']

    __lawn: Lawn
    __lawn_columns: int
    __lawn_rows: int

    __current_turn: int
    __moves_before_defeat: Optional[int]

    def __init__(self, lawn_raw: LawnRawT, zombies_raw: ZombieStatsRawT):
        self.__moves_before_defeat = None
        self.__init_lawn_data(lawn_raw)
        self.__lawn_columns = len(self.__lawn[0])
        self.__lawn_rows = len(self.__lawn)
        print(self.__lawn_rows)
        print(self.__lawn_columns)
        self.__init_zombies_data(zombies_raw)
        self.__zombies_active = []
        self.__current_turn = 0

    def __init_lawn_data(self, lawn_raw: LawnRawT):
        lawn = []
        self.__sshooters = []
        self.__numbered_shooters = []
        for raw_index in range(0, len(lawn_raw)):
            raw = lawn_raw[raw_index]
            lawn_row = []
            self.__numbered_shooters.append([])
            for column_index in range(0, len(raw)):
                square = raw[column_index]
                if square == ' ':
                    lawn_row.append(None)
                elif square == 'S':
                    sshooter = SShooter(raw_index, column_index)
                    self.__sshooters.append(sshooter)
                    lawn_row.append(sshooter)
                elif square.isdigit():
                    numbered_shooter = NumberedShooter(raw_index, column_index, int(square))
                    self.__numbered_shooters[raw_index].append(numbered_shooter)
                    lawn_row.append(numbered_shooter)
            lawn.append(lawn_row)
        self.__lawn = lawn

    def __init_zombies_data(self, zombies_raw: ZombieStatsRawT):
        parsed_zombies = []
        for i in zombies_raw:
            parsed_zombies.append(Zombie(i[0], i[1], i[2], self.__lawn_columns - 1))
        self.__zombies_pending = parsed_zombies

    def simulate(self):
        self.__print_lawn()
        while True:
            self.__simulate_zombies_turn()
            self.__print_lawn()
            if self.__has_zombie_entered_house():
                self.__moves_before_defeat = self.__current_turn
                break
            self.__simulate_plants_turn()
            self.__print_lawn()
            if self.__has_plants_defeated_zombies():
                break
            self.__current_turn += 1

    def simulation_result(self):
        return self.__moves_before_defeat

    def __simulate_zombies_turn(self):
        self.__move_zombies()
        self.__make_zombies_appear()

    def __move_zombies(self):
        for zombie in self.__zombies_active:
            self.__lawn[zombie.row()][zombie.column()] = None
            zombie.move()
            self.__eat_shooter_at_position_of(zombie)
            self.__lawn[zombie.row()][zombie.column()] = zombie

    def __make_zombies_appear(self):
        pending_zombies_to_remove = []
        for zombie in self.__zombies_pending:
            if zombie.move_number() <= self.__current_turn:
                pending_zombies_to_remove.append(zombie)
                self.__zombies_active.append(zombie)
                self.__eat_shooter_at_position_of(zombie)
                self.__lawn[zombie.row()][zombie.column()] = zombie
        for zombie in pending_zombies_to_remove:
            self.__zombies_pending.remove(zombie)

    def __eat_shooter_at_position_of(self, zombie: Zombie):
        square = self.__lawn[zombie.row()][zombie.column()]
        if isinstance(square, NumberedShooter):
            self.__numbered_shooters[zombie.row()].remove(square)
        elif isinstance(square, SShooter):
            self.__sshooters.remove(square)

    def __has_zombie_entered_house(self):
        for zombie in self.__zombies_active:
            if zombie.has_entered_house():
                return True
        return False

    def __simulate_plants_turn(self):
        self.__simulate_numbered_shooters_turn()
        self.__simulate_sshooters_turn()

    def __simulate_numbered_shooters_turn(self):
        for row in range(0, self.__lawn_rows):
            total_strength = self.__total_numbered_shooters_strength_for(row)
            for column in range(0, self.__lawn_columns):
                square = self.__lawn[row][column]
                if not isinstance(square, Zombie):
                    continue
                total_strength = self.__shoot_at(square, total_strength)
                if total_strength == 0:
                    break

    def __total_numbered_shooters_strength_for(self, row: int):
        strength = 0
        for shooter in self.__numbered_shooters[row]:
            strength += shooter.strength()
        return strength

    def __simulate_sshooters_turn(self):
        for shooter in sorted(self.__sshooters, key=cmp_to_key(self.__compare_sshooters), reverse=True):
            print(shooter.column())
            print(shooter.row())
            until_upper_bound = shooter.row()
            until_lower_bound = self.__lawn_rows - shooter.row() - 1
            until_right_bound = self.__lawn_columns - shooter.column() - 1
            for i in range(1, min(until_right_bound + 1, until_upper_bound + 1)):
                square = self.__lawn[shooter.row() - i][shooter.column() + i]
                if not isinstance(square, Zombie):
                    continue

                self.__shoot_at(square, 1)
                break
            for i in range(1, min(until_right_bound + 1, until_lower_bound + 1)):
                square = self.__lawn[shooter.row() + i][shooter.column() + i]
                if not isinstance(square, Zombie):
                    continue
                self.__shoot_at(square, 1)
                break
            for i in range(1, until_right_bound + 1):
                square = self.__lawn[shooter.row()][shooter.column() + i]
                if not isinstance(square, Zombie):
                    continue
                self.__shoot_at(square, 1)
                break

    @staticmethod
    def __compare_sshooters(first: 'SShooter', second: 'SShooter'):
        if first.column() == second.column():
            return sign(second.row() - first.row())
        return sign(first.column() - second.column())

    def __shoot_at(self, zombie: Zombie, strength: int):
        left_strength = zombie.hit(strength)
        if zombie.is_dead():
            self.__zombies_active.remove(zombie)
            self.__lawn[zombie.row()][zombie.column()] = None
        return left_strength

    def __has_plants_defeated_zombies(self):
        return len(self.__zombies_active) == 0 and len(self.__zombies_pending) == 0

    def __print_lawn(self):
        str = ''
        for row in self.__lawn:
            for column in row:
                if isinstance(column, NumberedShooter):
                    str += column.strength().__str__()
                elif isinstance(column, SShooter):
                    str += 'S'
                elif isinstance(column, Zombie):
                    str += 'Z' + column.hp().__str__()
                else:
                    str += ' '
            str += '\n'
        print(str)
        print()
        for i in self.__zombies_active:
            print("Zombie " + i.hp().__str__() + " at position " + i.row().__str__() + " " + i.column().__str__())
        print()
