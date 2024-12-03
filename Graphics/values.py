from Graphics import rectangle, circle
from Graphics.dgraphics import cuboid, sphere


print("\nRectangle\n")
l=int(input("Enter the length of the rectangle:\n"))
b=int(input("Enter the breadth of the rectangle:\n"))

rectangle.arear(l,b)
rectangle.perir(l,b)


print("\nCircle\n")
r=int(input("Enter the radius of the circle:\n"))

circle.areac(r)
circle.peric(r)

print("\nCuboid\n")
l=int(input("Enter the length of the Cuboid:\n"))
b=int(input("Enter the breadth of the Cuboid:\n"))
h=int(input("Enter the length of the Cuboid:\n"))


cuboid.areacub(l,b,h)
cuboid.pericub(l,b,h)


print("\nsphere\n")
r=int(input("Enter the radius of the Sphere:\n"))

sphere.areas(r)
sphere.peris(r)



