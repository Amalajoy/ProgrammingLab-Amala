import math

base=int(input("enter base length of triangle"))
height=int(input("enter height of triangle"))
length=int(input("enter length of rectangle"))
breadth=int(input("enter breadth of rectangle"))
side=int(input("enter side of square"))
               
t_area = lambda base,height : 1/2*base*height
r_area = lambda length,breadth : length*breadth
s_area = lambda side : side*side

print("Area of Triangle :", t_area(base,height))
print("Area of Rectangle:", r_area(length,breadth))
print("Area of Square :", s_area(side))