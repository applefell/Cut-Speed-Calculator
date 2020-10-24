import math

diameter = float(input("What is the diameter of your cutting tool?"))
spindle_speed = float(input("What is your spindle speed?"))

cut_speed = diameter * (math.pi/12) * spindle_speed

print("Your cutting speed is " + str(cut_speed) + " feet per minute.")