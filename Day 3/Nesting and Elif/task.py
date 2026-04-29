print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("You can ride the rollercoaster")
        if age <= 14:
            print("pay 4 lek")
        else:
            print("pay 7 lek ")
    else:
        print("You can't ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")
