import math 

def move_forward(direction,curr_x, curr_y):
    # Move the object forward by the given distance.
    radian_angle = math.radians(direction)
    curr_x +=  math.sin(radian_angle)
    curr_y +=  math.cos(radian_angle)
    return round(curr_x), round(curr_y)
    
def rotate_left(data):
    # Rotate the object left (counter-clockwise) by the given angle in degrees.
    return (data - 90)

def rotate_right(data):
    # Rotate the object right (clockwise) by the given angle in degrees.
    return (data + 90)