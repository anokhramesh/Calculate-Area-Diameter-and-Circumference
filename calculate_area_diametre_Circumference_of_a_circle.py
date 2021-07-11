print("A program for calculate the Area,Diameter and Circumference of a circle if Radius is known")
print("******************************************************************************************")
while True:
    pi = 3.14
    r = float(input("\nEnter the Radius\n"))
    a = float(pi*r)*r
    d = (2*r)
    c = float(2*pi*r)
    print ("The Area of Circle is",a)
    print ("The Diameter of Circle is ",d)
    print ("The Circumference of Circle is",c)