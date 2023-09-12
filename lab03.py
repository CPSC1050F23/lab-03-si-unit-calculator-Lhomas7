"""
Welcome to Lab 03.
knkjnjknjknl
We will be grading for Header, Comments, Formatting.

Follow the instructions in the lab document. 
Write your code to complete the tests in the Gradescope autograder.


Necessary statements:

"Please select one of the following to convert to meters: cm m km in ft: "
"Please select one of the following to convert to grams: mg g kg lbs: "
"Please select one of the following to convert to meters per second: m/s km/h ft/s mph: "
"Please select one of the following to convert to Celcius: C F K: "

"Please input a value: "
"Unsupported unit"
"Invalid unit type"

"""

print("Welcome to the convert to SI units calculator!")

print("Please input a type of unit that you would like to convert. Here are your options: \ndistance \nmass \nspeed \ntemperature\n")

"""get input"""
type_unit = input().strip()

"""ask user for conversion units and converts to meters"""
if type_unit == 'distance':
    print("Please select one of the following to convert to meters: cm m km in ft:")
    unit = input().strip()
    if unit == 'cm':
        print("Please input a value:")
        value = input().strip()
        conv = value / 100
        print(f'{value:.2f} {unit} in meters: {conv:.2f}')
    elif unit == 'm':
        print("Please input a value:")
        value = input().strip()
        conv = value
        print(f'{value:.2f} {unit} in meters: {conv:.2f}')
    elif unit == 'km':
        print("Please input a value:")
        value = input().strip()
        conv = value * 1000
        print(f'{value:.2f} {unit} in meters: {conv:.2f}')
    elif unit == 'in':
        print("Please input a value:")
        value = input().strip()
        conv = value * 0.0254
        print(f'{value:.2f} {unit} in meters: {conv:.2f}')
    elif unit == 'ft':
        print("Please input a value:")
        value = input().strip()
        conv = value * 0.3048
        print(f'{value:.2f} {unit} in meters: {conv:.2f}')
    else:
        print("Unsupported unit")







"""ask user for conversion units and convert to grams"""
if type_unit == 'mass':
    print("Please select one of the following to convert to grams: mg kg lbs:")
    unit = input().strip()
    if unit == 'mg':
        print("Please input a value:")
        value = input().strip()
        if value < 0:
            print("You can't have a negative mass!")
        else:
            conv = value / 1000
            print(f'{value:.2f} {unit} in grams: {conv:.2f}')
    elif unit == 'kg':
        print("Please input a value:")
        value = input().strip()
        if value < 0:
            print("You can't have a negative mass!")
        else:
            conv = value * 1000
            print(f'{value:.2f} {unit} in grams: {conv:.2f}')
    elif unit == 'lbs':
        print("Please input a value:")
        value = input().strip()
        if value < 0:
            print("You can't have a negative mass!")
        else:
            conv = value * 453.592
            print(f'{value:.2f} {unit} in grams: {conv:.2f}')
    else:
        print("Unsupported unit")





"""ask user for conversion units and converts to meters per second"""
if type_unit == 'speed':
    print("Please select one of the following to convert to meters per second: km/h ft/s miles/hour:")
    unit = input().strip()
    if unit == 'km/h':
        print("Please input a value:")
        value = input().strip()
        conv = value * 0.277778
        print(f'{value:.2f} {unit} in meters per second: {conv:.2f}')
    elif unit == 'ft/s':
        print("Please input a value:")
        value = input().strip()
        conv = value * 0.3048
        print(f'{value:.2f} {unit} in meters per second: {conv:.2f}')
    elif unit == 'miles/hour':
        print("Please input a value:")
        value = input().strip()
        conv = value * 0.44704
        print(f'{value:.2f} {unit} in meters per second: {conv:.2f}')
    else:
        print("Unsupported unit")




"""ask user for conversion units and convert to Celsius"""
if type_unit == 'temperature':
    print("Please select one of the following to convert to Celcius: F K:")
    unit = input().strip()
    if unit == 'F':
        print("Please input a value:")
        value = input().strip()
        conv = (value - 32) * 5/9
        print(f'{value:.2f} {unit} in Celsius: {conv:.2f}')
    elif unit == 'K':
        print("Please input a value:")
        value = input().strip()
        conv = value - 273.15
        print(f'{value:.2f} {unit} in Celsius: {conv:.2f}')
    else:
        print("Unsupported unit")


"""print invalid unit type if unit is type of unit that can't be converted"""
else:
    print("Invalid unit type")



