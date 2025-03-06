import re 

class field_setup:
    def __init__(self):
        self.width = 0
        self.height = 0

    def start(self):
        while True:
            user_input = input(
            f'''Welcome to Auto Driving Car Simulation!
            \nPlease enter the width and height of the simulation field in x y format:\n''').strip()
            
            try:
                # Regular expression to match exactly two integers separated by space
                if re.fullmatch(r"\d+ \d+", user_input):
                    
                    # Split the input and convert to integers
                    num1, num2 = map(int, user_input.split())
                    
                    # Check if both integers are within the specified range  
                    print(f"You have created a field of {num1} x {num2}.")

                    self.width = num1
                    self.height = num2
                    break
                else:
                    raise ValueError("Invalid input. Please enter exactly two positive integers separated by a space.")

            except ValueError as e:
                print(f"Error: {e}")

class car_setup:
    def __init__(self, field, registry):
        self.car_name(registry)
        self.car_position(field, registry)
        self.car_commands()
        self.collided = ""
        self.step = 0

    def car_name(self, data):
        while True:
            try:
                input_name = input("Please input the name of the car:\n").strip().upper()
                # to check if car names exists in current list
                if input_name in [car.name for car in data]:
                    raise ValueError("This name already exists. Please try again")
                else:
                    self.name = input_name
                    break
                    
            except ValueError as e:
                print(f"Error: {e}")    

    def car_position(self, field, data):
        while True: 
            try:
                initial_pos = input(f"Please enter initial position of car {self.name} in x y Direction format:\n").strip().upper()
                
                # to ensure position given are in the correct format
                if not re.fullmatch(r"\d+ \d+ [NSEW]", initial_pos):
                    raise ValueError("Error. Please try again in the correct format for the 3 variables - x y direction(NSEW only).\n")
                    continue
                
                xi, yi, di = initial_pos.split()

                # to ensure position given are not already occupied
                if f"{xi} {yi}" in [ f"{car.final_x} {car.final_y}" for car in data]:
                    raise ValueError("Location already occupied. Please start at a new location")
                # ensure position given are within the initial boundary           
                elif int(xi) > field.width or int(yi) > field.height or int(xi) < 0 or int(yi) < 0 :
                    raise ValueError(f"Impossible initial position. The simulation field size is {field.width} x {field.height}. Please try again.")            
                else: 
                    self.initial_x = self.final_x = int(xi)
                    self.initial_y = self.final_y = int(yi)
                    self.initial_dir = self.final_dir = di
                    break

            except ValueError as e:
                print(f"Error: {e}")


    def car_commands(self):
        while True:
            try:
                direction = input(f"Please enter the commands for car {self.name}:\n").strip().upper()
                # to ensure comands given are in correct format 
                if re.fullmatch(r"[LRF]+", direction):
                    # data format : [ 'car name','final position', 'command', 'step','collided cars','initial position' ]
                    # answer = [car_name, f"({xi},{yi}) {di.upper()}", direction.upper(),0,'0',f"({xi},{yi}) {di.upper()}"]
                    self.commands = direction
                    break
                else:
                    raise ValueError(
                        """Error. Please try again in the combination of [L][R][F] only
                        \nL: rotates the car by 90 degrees to the left
                        \nR: rotates the car by 90 degrees to the right
                        \nF: moves forward by 1 grid point\n""")
            except ValueError as e:
                print(f"Error: {e}")