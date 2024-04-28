from typing import Optional

from Rectangular import Rectangular, Point


def read_boundary_coordinates_input() -> Rectangular:
    rectangular = None
    while not rectangular:
        rectangular = try_read_single_boundary_coordinates_input()
    return rectangular


def try_read_single_boundary_coordinates_input() -> Optional[Rectangular]:
    try:
        rectangular = read_single_boundary_coordinates_input()
        return rectangular
    except ValueError:
        print("Bad input!\n")
        return None


def read_single_boundary_coordinates_input() -> Rectangular:
    upper_left_x = float(input("Welcome to Mandelbrot image creator!\nPlease enter coordinates of "
                               "upper left and lower right points of boundary rectangle!\n"))
    upper_left_y = float(input())
    lower_right_x = float(input())
    lower_right_y = float(input())
    if not check_boundary_input_correctness(upper_left_x, upper_left_y, lower_right_x, lower_right_y):
        raise ValueError()

    return Rectangular(Point(upper_left_x, upper_left_y), Point(lower_right_x, lower_right_y))


def check_boundary_input_correctness(upper_left_x: float, upper_left_y: float, lower_right_x: float,
                                     lower_right_y: float) -> bool:
    return upper_left_x < lower_right_x and lower_right_y < upper_left_y
