import re 

def field_check():
    while True:
        user_input = input(
        f'''Welcome to Auto Driving Car Simulation!
        \nPlease enter the width and height of the simulation field in x y format:\n''')
        
        # Regular expression to match exactly two integers separated by space
        if re.fullmatch(r"\d+ \d+", user_input):
            
            # Split the input and convert to integers
            num1, num2 = map(int, user_input.split())
            
            # Check if both integers are within the specified range  
            print(f"You have created a field of {num1} x {num2}.")
            return num1, num2
        else:
            print("Invalid input. Please enter exactly two integers separated by a space.")


def main_menu():

    while True:
        result = input('''
        \nPlease choose from the following options:
        \n[1] Add a car to field
        \n[2] Run simulation\n''').strip()

        if result.isdigit() and (int(result) == 1 or int(result) == 2) :
            return int(result)
        else:
            print("\nPlease choose either [1] or [2] only")


def car_start(num1,num2,data):

    while True:
        car_name = input("Please input the name of the car:\n").strip().upper()
        if car_name in [a[0] for a in data]:
            overwrite_check = input("This name already exists, do you want to overwrite? Y/N").strip().upper()
            if overwrite_check == 'Y':
                #remove existing data
                data = [ a for a in data if a[0]!=car_name ]
            else:
                continue
            
        initial_pos = input(f"Please enter initial position of car {car_name} in x y Direction format:\n")

        # to ensure position given are in the correct format
        if re.fullmatch(r"\d+ \d+ [nsewNSEW]", initial_pos):

            # to ensure position given are not already occupied
            if initial_pos in [a[1] for a in data]:
                print("Location already occupied. Please start at a new location")
                continue

            # to ensure position given are within the initial boundary     
            xi, yi, di = initial_pos.split()
            if int(xi) <= num1 and int(yi) <= num2 and int(xi)>=0 and int(yi) >=0 :
                direction = input(f"Please enter the commands for car {car_name}:\n").strip()
            else: 
                print(f"Impossible initial position. The simulation field size is {num1} x {num2}. Please try again.\n")
                continue

            # to ensure comands given are in correct format
            if re.fullmatch(r"[lrfLRF]+", direction):
                return [car_name, f"({xi},{yi}) {di.upper()}", direction.upper()]
            else:
                print("Error. Please try again in the correct format.\n")
                
        else:
            print("Error. Please try again in the correct format for the 3 variables - x y direction(NSEW only) .\n")

