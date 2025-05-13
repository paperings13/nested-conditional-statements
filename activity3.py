print("Customise your ride")
print(" Select your ride ")
print("1. Bike")
print("2. Car")
ride = int(input(" Enter the number of your choice " ))
if ride == 1:
    print("What type of bike?")
    print("1. Scooter")
    print("2. Electric")
    bike_type = int(input("Enter your number of choice " ))
    if bike_type == 1:
        print("You have chosen Scooty")
    else:
        print("You have chosen Electric")
else:
    print("What type of car?")
    print("1. Covertible")
    print("2. SUV")
    car_type = int(input("Enter the number of your choice"))
    if car_type == 1 :
        print("You have chosen Convertible")
    else:
        print("You have chosen SUV")
print("Have a nice and safer trip!")



