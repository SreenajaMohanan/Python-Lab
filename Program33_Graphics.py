from Graphics.RectFunctions import*
from Graphics.CirFunctions import*
from Graphics.DGraphics.SphereFunctions import*
from Graphics.DGraphics.CuboidFunctions import *

#Rectangle
l = int(input("Enter Length : "))
b = int(input("Enter Breadth : "))
print("Rectangle Area = ", RectArea(l,b))
print("Rectangle Perimeter = ", RectPerimeter(l,b))

#Circle
r = int(input("Enter radius of circle : "))
print("Circle Area = ", CirArea(r))
print("Circle Perimeter = ", CirPerimeter(r))

#sphere
r = int(input("Enter radius of sphere : "))
print("Sphere Area = ", SpArea(r))
print("Sphere Volume = ", SpPerimeter(r))

#Cuboid
l = int(input("Enter Cuboid Length : "))
b = int(input("Enter Cuboid Breadth : "))
h = int(input("Enter Cuboid Height : "))
print("Cuboid Area = ",CubArea(l,b,h))
print("Cuboid Perimeter = ", CubPerimeter(l,b,h))
