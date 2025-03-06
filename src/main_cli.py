import re
from .initial_setup import field_setup, car_setup
from .simulation import run_simulation, display_cars

def selection_check(query):
    while True:
        try:
            check = input(query).strip()
            #to check the selection is either 1 or 2 only
            if check.isdigit() and (int(check) == 1 or int(check) == 2) :
                return check
            else:
                raise ValueError("Please enter either [1] or [2] only.")

        except ValueError as e:
            print(f"Error: {e}")


def base():
    field = field_setup()
    field.start()

    registry = []

    while True:

        # to show current list of cars if user already added cars into the field
        if registry:
            display_cars(registry)
        
        entry_menu = '''Please choose from the following options:
            \n[1] Add a car to field
            \n[2] Run simulation\n'''

        entry_check = selection_check(entry_menu)
        
        try:
            #to add cars into current list of cars
            if entry_check == '1':
                new_car = car_setup(field, registry)
                registry.append(new_car)
                continue
            elif not registry:
                #to check if user run simulation directly before adding any cars
                raise ValueError("No cars are added into the simulation yet.")
            else:
                #to add a marker tracking steps of car during looping and collision
                #registry format : [ 'car name','final position', 'command', 'step','collided cars','initial position' ]
                run_simulation(registry, field)

        except ValueError as e:
            print(f"Error: {e}")
            continue

        #to check if user wants to exit or restart the simulation
        exit_menu = '''Please choose from the following options:
                \n[1] Start over
                \n[2] Exit\n'''

        exit_check = selection_check(exit_menu)
        if exit_check == '1':
            field = field_setup()
            field.start()
            registry = []
            continue
        else:
            print("Thank you for running the simulation. Goodbye!\n")
            break


if __name__ == "__main__":
    base()