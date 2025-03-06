import math 

def move_forward(direction,curr_x, curr_y):
    # Move the object forward by the given distance.
    radian_angle = math.radians(direction)
    curr_x +=  math.sin(radian_angle)
    curr_y +=  math.cos(radian_angle)
    return round(curr_x), round(curr_y)

def display_cars(data):
    print("Your current list of cars are:")
    for car in data:
        print(f"- {car.name}, ({car.initial_x},{car.initial_y}) {car.initial_dir}, {car.commands}")


def clashing_cars(curr_car, data):
    #to extract all car positions in the list
    position_list = [ f"{car.final_x} {car.final_y}" for car in data ]

    #if length of list & set is not the same
    #that means there are cars at the same location, which meant collision
    if len(set(position_list)) != len(position_list):
        duplicates = []

        for car in data:
            position = f"{car.final_x} {car.final_y}"
            if position == f"{curr_car.final_x} {curr_car.final_y}" and car.name != curr_car.name:
                duplicates.append(f"{car.name}")  

        if duplicates:
            return duplicates
    return False