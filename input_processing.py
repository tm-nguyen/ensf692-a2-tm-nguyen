# input_processing.py
# TIEN NGUYEN, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
"""

This is a class that represents a program about a sensor in 
the car's vision system

Class attributes:

light : str
the current state of the traffic light: greem, yellow, or red

pedestrian : str
the current state of pedestrian presence: yes or no

vehicle : str
the current state of vehicle presence: yes or no

"""

class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"
        #pass
        

    """
    This function is used to updates the sensor status based on the user input.

    This function will provide options so the user can choose
    an option to change the status of the signal light according to color
    (green, yellow or red), a pedestrian (yes or no) or vehicle (yes or no).

    It also handles invalid inputs and allows re-entry until correct without 
    terminating the program.

    It also allows the user to terminate the program by inputting a value of 0.

    """
    def update_status(self):
        
        # Use while True to let the program run until the user enters 0 to end.
        while True:
            # Ask the user to select a value to start the program.
            object = input("\nAre changes are detected in the vision input?"
                       "\nSelect 1 for light, 2 for pedestrian, 3 for vehicle," 
                       "or 0 to end the program: ")
            
            if object == "0": # If the user inputs 0, the program will be terminated.
                print("Ending program. Goodbye.")
                break
            elif object not in ["0", "1", "2", "3"]: # Show an error message when the user enters an invalid value .
                print("You must select either 1, 2, 3 or 0.")
            else:
                # When user inputs a validate value. Ask for the specific changing.
                value = input("What change has been indentified? ")

                # Update the appropriate attribute for light based on the user's choice.
                if object == "1":
                    if value in ["green", "yellow", "red"]:
                        self.light = value
                    else:
                        print("Invalid vision change")
                # Update the appropriate attribute for pedestrian based on the user's choice.
                elif object == "2":
                    if value in ["yes", "no"]:
                        self.pedestrian = value
                    else:
                        print("Invalid vision change")
                # Update the appropriate attribute for vehicle based on the user's choice.
                elif object == "3":
                    if value in ["yes", "no"]:
                        self.vehicle = value
                    else:
                        print("Invalid vision change")
                
                # Print the message and all objects attribute.
                print_message(self)
            
# The sensor object should be passed to this function to print the action message and current status
"""
This function to print the action message and the current status of the sensor.

Its parameters

sensor:Sensor
The object that contain the current state information.
"""
def print_message(sensor):
    # Determine and print the action message based on the sensor's status
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\nSTOP")
        print(f"\nLight = {sensor.light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .")
    elif sensor.light == "green" and (sensor.pedestrian == "no" or sensor.vehicle == "no"):
        print("\nProceed")
        print(f"\nLight = {sensor.light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .")
    elif sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        print("\nCaution")
        print(f"\nLight = {sensor.light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .")
    else:
        print("No Record, will be more updating!")

# Complete the main function below
"""
This is the main function to run this program by initinalizing the sensor
and starting the input status updating
"""
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()  # Initialize the Sensor object
    sensor.update_status()  # Start the program based on user input

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()
