import re 
from src.direction import *

def clashing_cars(pnt, data):
    # check if any cars having matching location
    pnt_tmp = pnt[1].split()[0]
    data_tmp = [ [a[0], a[1].split()[0]] for a in data ]
    all_position = [ a[0] for a in data_tmp if a[1] == pnt_tmp and a[0] != pnt[0]]

    #to return False if list is empty, else return the list of collided cars
    if not all_position :
        return False 
    else:
        return all_position

def display_cars(data):
    print("Your current list of cars are:")
    for a in data:
        print(f"- {a[0]}, {a[1]}, {a[2]}")

def run_simulation(data, x, y):
    max_len = max([len(a[2]) for a in data])
    direction = {'N':0, 'E':90, 'S':180, 'W':270}
    
    # to loop through all possible commands 
    for a in range(max_len):
        
        # to loop through all cars
        for b in data:

            # to check if it's final position clashes with any existing car position in board
            # if True, the collided cars will be recorded, and further commands will be skipped
            check = clashing_cars(b,data)
            if check:
                # collided cars will be appended to the end of list for tracking 
                b[4]=check
                continue
      
            #to skip the loop if it went out of range
            elif len(b[2]) < a+1:
                continue
                      
            #extract current position and direction from list
            if b[5]=='0':
                curr_pos, curr_dir = b[1].split()
            else:
                curr_pos, curr_dir = b[5].split()
            digits = re.findall(r'\d+', curr_pos)
            curr_x, curr_y = list(map(int, digits))

            # calculation
            # to rotate or move base on the command
            if b[2][a] =='L':
                tmp = rotate_left(direction[curr_dir])
                curr_dir = [k for k, v in direction.items() if v == tmp][0]
            elif b[2][a] == 'R':
                tmp = rotate_right(direction[curr_dir])
                curr_dir = [k for k, v in direction.items() if v == tmp][0]
            else: 
                curr_x, curr_y =  move_forward(direction[curr_dir], curr_x, curr_y)
                
            # to skip updating car movement if it's final position exceeds board boundary
            if curr_x > x or curr_y > y or curr_x < 0 or curr_y < 0:
                continue

            # update car new position into the list 
            b[5] = f"({curr_x},{curr_y}) {curr_dir}"
            
            #record the step
            b[3] = (a+1)
    
    # display initial list and position
    display_cars(data)

    # output the result
    print("After simulation, the result is:")
    for a in data:
        if a[4] == '0':
            print(f"- {a[0]}, {a[5]}")
        else: 
            location = a[1].split()[0]
            col_cars = ", ".join(a[4])
            print(f"- {a[0]} , collided with {col_cars} at {location} at step {a[3]}")
