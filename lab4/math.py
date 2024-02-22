# ex 1
from math import pi
x = int(input())
y = 3.14
z = 180
degree = (x*y)/z
print(degree)

# ex 2
from math import pi
height = int(input())
a = int(input())
b = int(input())
expected_output = (height/2)*(a+b)
print(expected_output)

# ex 3
from math import tan, pi
def areaRegularPolygon(sides, length):
    area = int((sides * length ** 2) / (4 * tan(pi / sides)))
    return area

# ex 4
from math import pi
length = int(input())
heigth = int(input())
z = length*heigth
print(float(z))
