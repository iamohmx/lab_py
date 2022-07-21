# print(min(4,2,1))
# print(max(4,2,1))
# print(abs(-51))
# print(pow(4,3))

import math
from turtle import circle

# print(math.sqrt(16))
# print(math.floor(4.6))
# print(math.pi)

# y = math.sqrt(16 - 4 * x)
# y = math.sqrt(16 - 4 * pow(2))
# y = abs(15 - 50)

# s = u*t+1/2*a*t*pow(2)
# x = -b+math.sqrtb*pow(2)-4*a*c


# absnum = float(input())
# print(abs(absnum))
# print(abs(math.floor(absnum)))

r = int(input("Enter a radius: "))

area = math.pi * r ** 2

circum = 2 * math.pi * r

print("Area of a circle with radius %d is %.2f" % (r, area))
print("Circumference of a circle with radius %d is %.2f" % (r,circum))