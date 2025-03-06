import re 
from src.direction import *

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
        else:
            return False
    else:
        return False


def display_cars(data):
    print("Your current list of cars are:")
    for car in data:
        print(f"- {car.name}, {car.final_x} {car.final_y} {car.final_dir}, {car.commands}")

def run_simulation(data, field):
    max_len = max([len(car.commands) for car in data])
    direction = {'N':0, 'E':90, 'S':180, 'W':270}
    
    # to loop through all possible commands 
    for a in range(max_len):
        
        # to loop through all cars
        for car in data:

            # to check if it's final position clashes with any existing car position in board
            # if True, the collided cars will be recorded, and further commands will be skipped
            check = clashing_cars(car, data)
            if check:
                # collided cars will be appended to the end of list for tracking 
                car.collided = check
                continue
      
            #to skip the loop if it went out of range
            elif len(car.commands) < a+1:
                continue
                      
            # calculation
            # to rotate or move base on the command
            if car.commands[a] =='L':

                tmp = rotate_left(direction[car.final_dir])
                curr_dir = [k for k, v in direction.items() if v == tmp][0]
                car.final_dir = curr_dir

            elif car.commands[a] == 'R':

                tmp = rotate_right(direction[car.final_dir])
                curr_dir = [k for k, v in direction.items() if v == tmp][0]
                car.final_dir = curr_dir

            else: 
    
                curr_x, curr_y =  move_forward(direction[car.final_dir], car.final_x, car.final_y)
                # to skip updating car movement if it's final position exceeds board boundary
                if curr_x > field.width or curr_y > field.height or curr_x < 0 or curr_y < 0:
                    car.step = a + 1
                    continue
                else:
                    car.final_x = curr_x
                    car.final_y = curr_y

            final_check = clashing_cars(car, data)
            if final_check:
                # collided cars will be appended to the end of list for tracking 
                car.collided = final_check
            #record the step
            car.step = a + 1




    # display initial list and position
    display_cars(data)

    # output the result
    print("After simulation, the result is:")
    for car in data:
        if not car.collided:
            print(f"- {car.name}, ({car.final_x},{car.final_y}) {car.final_dir}")
        else: 
            location = f"{car.final_x} {car.final_y}"
            col_cars = ", ".join(car.collided)
            print(f"- {car.name} , collided with {col_cars} at ({car.final_x},{car.final_y}) at step {car.step}")
