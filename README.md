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

## Files
- auto_driving.md: Full brief of the questions and scenarios of this program is required to solve.
- requirements.txt: List package required to run the program smoothly.
- main.py: main running file. Program will be started by running this file
- direction.py: sub-module file. Rotate and/or move the cars according to commands
- initial_setup.py: sub-module file. Records and setup the name, initial position, and car commands
- simulation.py: sub-module file. Run through the car commands to get the final location.
- sandbox.ipynb: ipython notebook. Able to test and tryout codes.

## Criteria
- Code quality should be production ready and with the necessary unit tests.
- Coding style should follow software engineering best practice that the candidate is doing.
