from turtle import fd, right, left, bk
import math


BASE_TO_SIDES_ANGLE_DEG = 60
RAM_ANGLE = 30

get_extra_top_floor_length = lambda angle, sides_height: math.sin(math.radians(90 - angle)) * sides_height


SAIL_RIGHT = "RIGHT"
SAIL_LEFT = "LEFT"


def ship_base(floor_length, sides_height, ram_size=None):
    fd(floor_length)
    left(BASE_TO_SIDES_ANGLE_DEG)
    fd(sides_height)
    left(180 - BASE_TO_SIDES_ANGLE_DEG)
    
    extra_top_floor_length = get_extra_top_floor_length(BASE_TO_SIDES_ANGLE_DEG, sides_height)
    
    fd(extra_top_floor_length * 2)
    fd(floor_length)
    left(180 - BASE_TO_SIDES_ANGLE_DEG)
    fd(sides_height)
    bk(sides_height)
    
    left(BASE_TO_SIDES_ANGLE_DEG)
    if ram_size is not None:
        left(180 - BASE_TO_SIDES_ANGLE_DEG + RAM_ANGLE)
        fd(ram_size)
        bk(ram_size)
        right(180 - BASE_TO_SIDES_ANGLE_DEG + RAM_ANGLE)
    
    fd(extra_top_floor_length + floor_length / 2)
    left(90)
        


def ship_mast(mast_height, ship_sail_builder, triangle_size):
    fd(mast_height)
    ship_sail_builder(SAIL_LEFT, triangle_size)
    bk(mast_height)
    


def ship_sail(sail_direction, triangle_size):
    angle_command = right if sail_direction == "LEFT" else left
    angle_command(180)
    
    angle_command(60)
    fd(triangle_size)
    angle_command(210)
    fd(triangle_size * math.sin(math.radians(60)))
    angle_command(270)
    fd(triangle_size/2)
    
    


if __name__ == "__main__":
    ship_base(300, 90, 60)
    ship_mast(180, ship_sail, 210)
    
    
    