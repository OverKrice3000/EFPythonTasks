from constants import IMAGE_HEIGHT, IMAGE_WIDTH, EPSILON
from imageCreationUtils import write_file_header, write_image_header, write_image_info
from inputUtils import read_boundary_coordinates_input

if __name__ == '__main__':
    rectangular = read_boundary_coordinates_input()
    horizontal_shift = (rectangular.lower_right().x() - rectangular.upper_left().x()) / IMAGE_WIDTH
    vertical_shift = (rectangular.upper_left().y() - rectangular.lower_right().y()) / IMAGE_HEIGHT
    image_width = IMAGE_WIDTH
    image_height = IMAGE_HEIGHT
    if horizontal_shift - vertical_shift > EPSILON:
        image_height = int(image_height * (vertical_shift / horizontal_shift))
        vertical_shift = horizontal_shift
    elif vertical_shift - horizontal_shift > EPSILON:
        image_width = int(image_width * (horizontal_shift / vertical_shift))
        horizontal_shift = vertical_shift

    bmp = open("bmp.bmp", "wb+")
    write_file_header(bmp, image_width, image_height)
    write_image_header(bmp, image_width, image_height)
    write_image_info(bmp, rectangular, image_width, image_height, horizontal_shift, vertical_shift)
