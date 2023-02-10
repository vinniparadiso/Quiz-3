#authors are Gabby and Vinni
#Problem 5
def net_value(salary):
    value=0.14*(salary-100)+0.24*(salary+1000)
    print(value)

net_value(10)

#Problem 6
def next_stop(location):
    print("Next stop is", location)

def repeat_next_stop(location):
    next_stop(location)
    next_stop(location)

repeat_next_stop("Chicago")

#Problem 7
import math
def area_circle(radius):
    area=math.pi*radius**2
    circum=2*math.pi*radius
    circle=area-circum
    print(circle)

area_circle(10)

#Problem 8

def greetings(name):
    print("Hello", name)

greetings("Gabby and Vinni!")

#Problem 9
import math
def angle(x):
    value=math.sin(x)**3+math.cos(x)-3*(math.tan(x)/(math.tan(x)+1)**2)
    print(value)

angle(25)
