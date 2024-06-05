from datetime import datetime
import math

current_date_and_time= datetime.now(tz=None)
pi= math.pi
width=int(input("Enter the width of the tire in mm (ex 205): "))
ratio= int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter= int(input("Enter the diameter of the wheel in inches (ex: 15): "))

formula_upper_part= pi * width**2 * ratio * (width*ratio + 2540*diameter)
total= formula_upper_part/10000000000

print(f"The approximate volume is {total:.2f} liters")

with open("volumes.txt" , "at") as volume_file:
    print("Date - width - ratio - diameter - total", file = volume_file)
    print(f"{current_date_and_time}, {width} , {ratio} , {diameter} , {total}", file = volume_file)

finish=False;
while not finish:
    buy_tire=input("Do you want to buy the tires with the dimensions you enter?: ")
    if buy_tire.lower()=="yes":
        name= input("Please give us your full name: ")
        phone=input("please give us your phone number to contact you: ")
        with open("volumes.txt" , "at") as volume_file:
            print(f"{name} wants to bought the tire above please contact her/him with this phone number {phone}", file=volume_file)
        finish=True;
    elif buy_tire.lower()=="no":
        print("okay thank you, have a nice day :)")
        finish=True;
    else:
        print("PLEASE ENTER A VALID OPTION!!!")
    