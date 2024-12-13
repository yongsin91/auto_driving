#!/usr/bin/env python
# coding: utf-8

import re
from initial_setup import *
from simulation import *

def main():
    num1, num2 = field_check()
    registry = []
    loop1 = True
    loop2 = True
    while loop1 :
        selection = main_menu()
        
        if selection == 1:
            registry.append(car_start(num1,num2, registry))
        else: 
            #to add a marker tracking steps of car during looping and collision
            #registry format : [ 'car name','car position', 'command', 'step','collided cars' ]
            registry = [ b + [0] + ['0'] for b in registry ]
            result = run_simulation(registry, num1, num2)

            while loop2:
                check = input('''
                \nPlease choose from the following options:
                \n[1] Start over
                \n[2] Exit\n''').strip()
    
                if check =='1':
                    registry = []
                    loop2 = False 
    
                elif check =='2':
                    loop1 = False
                    loop2 = False 
                else:
                    print("Please enter either [1] or [2] only.")

            loop2 = True


main()

