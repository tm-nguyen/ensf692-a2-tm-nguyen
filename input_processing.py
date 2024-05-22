# input_processing.py
# YOUR NAME, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"
        #pass


    # Replace these comments with your function commenting
    def update_status(self): # You may decide how to implement the arguments for this function
        while True:
            object = input("\nAre changes are detected in the vision input?"
                       "\nSelect 1 for light, 2 for pedestrian, 3 for vehicle," 
                       "or 0 to end the program: ")
            if object not in ["0", "1", "2", "3"]:
                print("You must select either 1, 2, 3 or 0.")
            elif object == "0":
                print("Ending program. Goodbye.")
                break
            else:
                value = input("What change has been indentified? ")

                if object == "1":
                    if value in ["green", "yellow", "red"]:
                        self.light = value
                        print_message(self)
                    else:
                        print("Invalid vision chnage")
                        print_message(self)
                elif object == "2":
                    if value in ["yes", "no"]:
                        self.pedestrian = value
                        print_message(self)
                    else:
                        print("Invalid vision chnage")
                        print_message(self)
                elif object == "3":
                    if value in ["yes", "no"]:
                        self.vehicle = value
                        print_message(self)
                    else:
                        print("Invalid vision chnage")
                        print_message(self)

# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
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
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()
    sensor.update_status()

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()
