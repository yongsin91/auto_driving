#!/usr/bin/env python
# coding: utf-8

import re
from src.initial_setup import field_check, main_menu, car_start
from src.simulation import run_simulation, display_cars

def main():
    num1, num2 = field_check()
    registry = []
    loop1 = True
    loop2 = True
    while loop1 :

        # to show current list of cars if user already added cars into the field
        if registry:
            display_cars(registry)

        selection = main_menu()
        
        #to add cars into current list of cars
        if selection == 1:
            registry.append(car_start(num1,num2, registry))
        else: 
            
            #to check if user run simulation directly before adding any cars
            if not registry:
                print("No cars are added into the simulation yet.")
            else:
                #to add a marker tracking steps of car during looping and collision
                #registry format : [ 'car name','car position', 'command', 'step','collided cars' ]
                registry = [ b + [0] + ['0'] for b in registry ]
                result = run_simulation(registry, num1, num2)

                #to check if user wants to exit or restart the simulation
                while loop2:
                    check = input(
                        '''\nPlease choose from the following options:
                        \n[1] Start over
                        \n[2] Exit\n''').strip()

                    #to restart the simulation
                    if check =='1':
                        registry = []
                        loop2 = False 
                        
                    #to exit the simulation
                    elif check =='2':
                        loop1 = False
                        loop2 = False 
                    else:
                        print("Please enter either [1] or [2] only.\n")

                loop2 = True


main()

