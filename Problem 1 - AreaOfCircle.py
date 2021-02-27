#Justin Mitchell
#2/22/2021

#Problem 1 Area of a Circle

import math


def areaOfCircle(radius):
  return math.pi * radius ** 2


r = float(input(" Please enter the radius of a circle: "))

area = areaOfCircle(r)

print(" Area Of a Circle = %.2f" %area)


#Program asks the user to enter the radius of the circle, then the area of the circle is provided to user.

