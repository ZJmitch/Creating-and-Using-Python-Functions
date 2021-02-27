#Justin Mitchell
#2/23/2021

#Problem 3 multiple all the numbers in a list

import math

def multiplyList(myList):

    result = 1
    for x in (myList):
            result = result * x
    return result


list1 = [5, 2, 7, -1]

val = multiplyList(list1)

print(val)


#Program reads created multiplyList function, I set val = results, Print val to get problem solved.
