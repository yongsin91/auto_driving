import unittest
import io

from unittest.mock import patch

from src.initial_setup  import field_setup, car_setup
from src.misc           import move_forward, display_cars, clashing_cars, rotate_dir
from src.simulation     import run_simulation
from src.main_cli       import selection_check, base

# Dummy field class to simulate the field object
class DummyField:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Dummy car class to simulate the car object
class DummyCar:
    def __init__(self, name, final_x, final_y, final_dir, commands):
        self.name = name
        self.final_x = self.initial_x = final_x
        self.final_y = self.initial_y = final_y
        self.final_dir = self.initial_dir = final_dir
        self.commands = commands
        self.collided = False
        self.step = 0

# Unit tests for field_setup
class TestFieldSetup(unittest.TestCase):
    
    # input tested on invalid format input, empty inputs followed by a valid input.
    @patch('builtins.input', side_effect=["10", "abc", "", "15 25"])
    def test_invalid_then_valid_input(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            fs = field_setup()
            fs.start()
            output = fake_out.getvalue()
            # Check that error messages appear for invalid inputs
            self.assertIn("Error: Invalid input. Please enter exactly two positive integers separated by a space.", output)
            # And finally, that the valid input is accepted
            self.assertIn("You have created a field of 15 x 25.", output)
            self.assertEqual(fs.width, 15)
            self.assertEqual(fs.height, 25)

    # ENHANCED: input tested on 0 x 0 field
    @patch('builtins.input', side_effect=["0 0","15 25"])
    def test_enhanced_zerofield(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            fs = field_setup()
            fs.start()
            output = fake_out.getvalue()
            # Check that error messages appear for invalid inputs
            self.assertIn("Invalid input. please enter more than 0 x 0", output)
            # And finally, that the valid input is accepted
            self.assertIn("You have created a field of 15 x 25.", output)
            self.assertEqual(fs.width, 15)
            self.assertEqual(fs.height, 25)

# Unit tests for car_setup
class TestCarSetup(unittest.TestCase):
 
    # input tested on duplicating car names, empty car names 
    @patch('builtins.input', side_effect=["Car1", "", "Car2", "1 2 N", "LrF"])
    def test_car_duplicate_name(self, mock_input):
        car1 = DummyCar("CAR1", "0", "0", "N", "F")
        registry = [car1]
        field = DummyField(10, 10)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            car = car_setup(field, registry)
            output = fake_out.getvalue()
            self.assertIn("Empty field received. Please enter a name",output)
            self.assertEqual(car.name, "CAR2")
    
    # input tested on wrong position format, invalid input, empty input, overlapping position 
    @patch('builtins.input', side_effect=["Car2", "invalid", " 5 4 a ", "0 0 s ", "", "1 2 N", "LrF"])
    def test_car_wrong_position(self, mock_input):
        car1 = DummyCar("CAR1", "0", "0", "N", "F")
        registry = [car1]
        field = DummyField(10, 10)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            car = car_setup(field, registry)
            self.assertEqual(car.final_x, 1)
            self.assertEqual(car.final_y, 2)
            self.assertEqual(car.final_dir, "N")


    # ENHANCED: input tested on out of bounds position ( 2 x 2 ) for field size only 2 x 2
    @patch('builtins.input', side_effect=["Car2", "2 2 n", "1 1 N", "LrF"])
    def test_car_enhanced_wrong_position(self, mock_input):
        registry = []
        field = DummyField(2, 2)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            car = car_setup(field, registry)
            output = fake_out.getvalue()
            self.assertIn('Error: Impossible initial position. The simulation field size is 2 x 2. Please try again.\n', output)
            self.assertEqual(car.final_x, 1)
            self.assertEqual(car.final_y, 1)
            self.assertEqual(car.final_dir, "N")

    # input tested on invalid commands, empty commands
    @patch('builtins.input', side_effect=["Car2", "1 2 N", "abc", "", "LrF"])
    def test_invalid_commands(self, mock_input):
        registry = []
        field = DummyField(10, 10)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            car = car_setup(field, registry)
            self.assertEqual(car.commands, "LRF")

# Unit tests for move_forward
class TestMoveForward(unittest.TestCase):
    # Tests for move_forward in both x and y axis
    def test_move_forward(self):
        result = move_forward(0, 0, 0)
        self.assertEqual(result, (0, 1))
        result = move_forward(90, 0, 0)
        self.assertEqual(result, (1, 0))    
        result = move_forward(180, 0, 0)
        self.assertEqual(result, (0, -1)) 
        result = move_forward(270, 0, 0)
        self.assertEqual(result, (-1, 0))
        result = move_forward(0, 5, 5)
        self.assertEqual(result, (5, 6))

# Unit tests for clashing_cars
class TestClashingCars(unittest.TestCase):
    def test_clashing_cars_no_collision(self):
        car1 = DummyCar("A", 1, 1, "N", "F")
        car2 = DummyCar("B", 2, 2, "N", "F")
        data = [car1, car2]
        result = clashing_cars(car1, data)
        self.assertFalse(result)

    def test_clashing_cars_with_collision(self):
        car1 = DummyCar("A", 1, 1, "N", "F")
        car2 = DummyCar("B", 1, 1, "N", "F")
        data = [car1, car2]
        result = clashing_cars(car1, data)
        # Expect car1 to detect collision with car2.
        self.assertEqual(result, ["B"])

# Unit tests for display_cars
class TestDisplayCars(unittest.TestCase):
    def test_display_cars(self):
        car1 = DummyCar("A", 1, 1, "N", "F")
        car2 = DummyCar("B", 2, 2, "E", "LFR")
        data = [car1, car2]
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            display_cars(data)
            output = fake_out.getvalue()
            self.assertIn("Your current list of cars are:", output)
            self.assertIn("- A, (1,1) N, F", output)
            self.assertIn("- B, (2,2) E, LFR", output)

# Unit tests for rotate_dir
class TestRotateDir(unittest.TestCase):
    def test_rotate_left(self):
        # Test left rotations.
        self.assertEqual(rotate_dir('L', 0), 270)
        self.assertEqual(rotate_dir('L', 90), 0)
        self.assertEqual(rotate_dir('L', 180), 90)
        self.assertEqual(rotate_dir('L', 270), 180)
        
    def test_rotate_right(self):
        # Test right rotations.
        self.assertEqual(rotate_dir('R', 0), 90)
        self.assertEqual(rotate_dir('R', 90), 180)
        self.assertEqual(rotate_dir('R', 180), 270)
        self.assertEqual(rotate_dir('R', 270), 0)

# Unit tests for the run_simulation
class TestSimulation(unittest.TestCase):
    def test_run_simulation_collision(self):
        carA = DummyCar("A", 1, 1, "N", "FLRF")
        carB = DummyCar("B", 1, 2, "S", "FRRLRFF")
        data = [carA, carB]
        field = DummyField(10, 10)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            run_simulation(data, field)
            output=fake_out.getvalue()
            self.assertIn("- A , collided with B at (1,2) at step 1", output)
            self.assertIn("- B , collided with A at (1,2) at step 0", output)
            self.assertTrue(carA.collided and carB.collided)
            # Verify car did not move after collision
            self.assertTrue(carA.step > 0)
            self.assertEqual(carB.step, 0)

    def test_run_simulation_no_collision(self):
        carA = DummyCar("A", 1, 1, "N", "F")
        carB = DummyCar("B", 2, 9, "E", "FLFFFRF")
        data = [carA, carB]
        field = DummyField(10, 10)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            run_simulation(data, field)
            # Car A: Facing North ('N') moves from (1,1) to (1,2). Expect step to not increase after car A stop.
            self.assertEqual(carA.final_x, 1)
            self.assertEqual(carA.final_y, 2)
            self.assertEqual(carA.step,1)
            # Car B: Facing East ('E') move it from (2,9) to (4,10).
            # Expect car will not move out of bounds during step 4 & 5, but rotate right at step 6 and move.
            # Expect steps are still counted although car is not moving due to out of bounds
            self.assertEqual(carB.final_x, 4)
            self.assertEqual(carB.final_y, 9)
            self.assertEqual(carB.step,7)

# Unit tests for the base
class TestBase(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        # Field setup: prompt for width and height.
        "10 10",
        # First menu: choose to add a car.
        "1",
        # Car setup: car_name prompt.
        "TestCar",
        # Car setup: car_position prompt.
        "1 1 N",
        # Car setup: car_commands prompt.
        "F",
        # Second menu iteration: choose to run simulation.
        "2",
        # Exit menu: choose to exit.
        "2"
    ])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_base_exit_flow(self, mock_stdout, mock_input):
        # Run the base function which will use the above simulated inputs.
        base()
        
        # Get all printed output.
        output = mock_stdout.getvalue()
        self.assertIn("Thank you for running the simulation. Goodbye!", output)

# Unit tests for selection_check
class TestSelectionCheck(unittest.TestCase):
    def test_valid_input(self):
        # When the input is valid immediately
        with patch('builtins.input', return_value='1'):
            result = selection_check("Choose 1 or 2: ")
            self.assertEqual(result, '1')

    @patch('builtins.input', side_effect=['abc', '2'])
    def test_invalid_then_valid_input(self, mock_input):
        # Simulate multiple inputs: first an invalid input, then a valid input.
        # Simulate only correct selections are being returned
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            result = selection_check("Choose 1 or 2: ")
            output = fake_out.getvalue()
            self.assertIn("Error: Please enter either [1] or [2] only.", output)
            self.assertEqual(result, '2')

if __name__ == '__main__':
    unittest.main()