import math 

def move_forward(direction,curr_x, curr_y):
    # Move the object forward by the given distance.
    radian_angle = math.radians(direction)
    curr_x +=  math.sin(radian_angle)
    curr_y +=  math.cos(radian_angle)
    return round(curr_x), round(curr_y)
    
def rotate(direction, data):
    # Rotate the object left (counter-clockwise) by the given angle in degrees.
    if direction == 'L':
        return (data - 90) % 360
    else:
        return (data + 90) % 360