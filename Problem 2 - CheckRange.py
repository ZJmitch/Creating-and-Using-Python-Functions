#Justin Mitchell
#2/22/2021

#Problem 2 check number in a given range

import math


def rangeNumber(n):


    if int(num) in range(1, 10):
        print ("You entered a number in the range of 1 to 10")
    elif int(num) not in range(1, 10):
        print("Your number was not in the range")
    return

num = int(input(" Enter a number:  "))

val = rangeNumber(num)


print(val)

#Program defines rangeNumber function then asks the user to input a number, result gets printed.

