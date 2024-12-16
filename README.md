# Auto Driving Car Simulation

## Objective
You are tasked with developing a simulation program for an autonomous driving car, with the aim of competing with Tesla. Your team has already developed a prototype car, but it is still in its primitive stage.

## Details
The simulation program is designed to work with a rectangular field, specified by its width and height. The bottom left coordinate of the field is at position (0,0), and the top right position is denoted (width,height). For example, a field with dimensions 10 x 10 would have its upper right coordinate at position (9,9).

One or more cars can be added to the field, each with a unique name, starting position, and direction they are facing. For instance, a car named "A" may be placed at position (1,2) and facing North.

A list of commands can be issued to each car, which can be one of three commands:
- L: rotates the car by 90 degrees to the left
- R: rotates the car by 90 degrees to the right
- F: moves forward by 1 grid point

If a car tries to move beyond the boundary of the field, the command is ignored, and the car stays in its current position. For example, if a car at position (0,0) is facing South and receives an F command, the command will be ignored as it would take the car beyond the boundary of the field.

## Requirements
- Python 3.4 or higher (regex full match introduced at 3.4)
- No additional dependencies are required (uses standard library modules).

## Setup Instruction 
- Clone this repository
- Run the main script: python main.py

## Files & Folders Details
### Main Directory 
- auto_driving.md: Full brief of the questions and scenarios of this program is required to solve.
- requirements.txt: List package required to run the program smoothly.
- main.py: main running file. Program will be started by running this file
### Src 
- direction.py: sub-module file. Rotate and/or move the cars according to commands
- initial_setup.py: sub-module file. Records and setup the name, initial position, and car commands
- simulation.py: sub-module file. Run through the car commands to get the final location.
### Notebooks
- sandbox.ipynb: ipython notebook. Able to test and tryout codes.

## Assumption
- Car names are case insensitive and unique therefore 'a' and 'A' will be considered as the same car. No 2 cars will have the same name.
- When processing commands for multiple cars, at every step, only one command can be processed for each car and it is sequential.
- When multiple collision occurs, will only record steps of earliest collisions <br>( i.e. if car A and C collides at step 3, then car B collides with car A at step 7, car A will only record step 3 )</br>
- When multiple collision occurs, will not show individual collision breakdown <br>( i.e. if car A and C collides at step 3, then car B collides with car A at step 7, car A will only show collision with both car B and C and car A stops at step 3 )</br>
- If user key in the same car name during the <ins>[1] Add a car to field</ins> phase, additional option is given to check if user want to overwrite current data.
- If car movement exceeds simulation boundary, the step will be skipped, but subsequent steps will still continue to be processed.
- Output results are all printed and shown but not logged. 
