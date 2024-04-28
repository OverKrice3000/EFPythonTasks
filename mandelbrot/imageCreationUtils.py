import sys
from typing import BinaryIO

from Rectangular import Point, Rectangular
from constants import IMAGE_HEADER_SIZE, FILE_HEADER_SIZE, IMAGE_DEPTH, IMAGE_HORIZONTAL_RESOLUTION, \
    IMAGE_VERTICAL_RESOLUTION


def define_point_color(point: Point) -> int:
    current_point = Point(0, 0)
    for i in range(50, 256):
        next_point_x = current_point.x() * current_point.x() - current_point.y() * current_point.y() + point.x()
        next_point_y = 2 * current_point.x() * current_point.y() + point.y()
        current_point = Point(next_point_x, next_point_y)
        if current_point.x() * current_point.x() + current_point.y() * current_point.y() > 4:
            return i
    return 0


def write_file_header(bmp: BinaryIO, image_width: int, image_height: int):
    bmp.write("BM".encode())
    sizeof_file = FILE_HEADER_SIZE + IMAGE_HEADER_SIZE + image_width * image_height * 4
    bmp.write(sizeof_file.to_bytes(4, sys.byteorder))
    reserved = 0
    bmp.write(reserved.to_bytes(4, sys.byteorder))
    image_shift = FILE_HEADER_SIZE + IMAGE_HEADER_SIZE
    bmp.write(image_shift.to_bytes(4, sys.byteorder))


def write_image_header(bmp: BinaryIO, image_width: int, image_height: int):
    sizeof_header = IMAGE_HEADER_SIZE
    bmp.write(sizeof_header.to_bytes(4, sys.byteorder))
    bmp.write(image_width.to_bytes(4, sys.byteorder))
    bmp.write(image_height.to_bytes(4, sys.byteorder))
    number_of_planes = 1
    bmp.write(number_of_planes.to_bytes(2, sys.byteorder))
    image_depth = IMAGE_DEPTH
    bmp.write(image_depth.to_bytes(2, sys.byteorder))
    compression_method = 0
    bmp.write(compression_method.to_bytes(4, sys.byteorder))
    sizeof_image = image_width * image_height * 4
    bmp.write(sizeof_image.to_bytes(4, sys.byteorder))
    horizontal_resolution = IMAGE_HORIZONTAL_RESOLUTION
    bmp.write(horizontal_resolution.to_bytes(4, sys.byteorder))
    vertical_resolution = IMAGE_VERTICAL_RESOLUTION
    bmp.write(vertical_resolution.to_bytes(4, sys.byteorder))
    num_of_colors = 0
    bmp.write(num_of_colors.to_bytes(4, sys.byteorder))
    num_of_important_colors = 0
    bmp.write(num_of_important_colors.to_bytes(4, sys.byteorder))


def write_image_info(bmp: BinaryIO, rectangular: Rectangular, image_width: int, image_height: int,
                     horizontal_shift: float, vertical_shift: float):
    current_x = rectangular.upper_left().x()
    current_y = rectangular.lower_right().y()
    reserved = 0
    for i in range(0, image_height):
        current_x = rectangular.upper_left().x()
        for j in range(0, image_width):
            iteration = define_point_color(Point(current_x, current_y))
            bmp.write(reserved.to_bytes(1, sys.byteorder))
            bmp.write(iteration.to_bytes(1, sys.byteorder))
            bmp.write(reserved.to_bytes(1, sys.byteorder))
            bmp.write(reserved.to_bytes(1, sys.byteorder))
            current_x += horizontal_shift
        current_y += vertical_shift
