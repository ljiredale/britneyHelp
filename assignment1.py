def multiply(n1, n2): #multiply two numbers
    return n1*n2
def divide(n1, n2): #divide two numbers
    return n1/n2
def subtract(n1, n2): #subtract two numbers
    return n1-n2
def volumeOfCube(w, l, h): #volume of a cube
    return w*l*h
def average(n1, n2, n3): #average of three numbers
    return (n1*n2*n3)/3

#multiply two numbers
print(multiply(3, 5))
print(multiply(4, 6))
#divide two numbers
print(divide(6, 3))
print(divide(8, 4))
#subtract two numbers
print(subtract(3, 4))
print(subtract(5, 3))
#volume of a cube
print(volumeOfCube(5, 4, 3))
print(volumeOfCube(7, 3, 5))
#average of three numbers
print(average(3, 4, 5))
print(average(6, 3, 8))

#two numbers input to multiply
m1 = input("First number you would like to multiply: ")
m2 = input("Second number you would like to multiply: ")
print(multiply(int(m1), int(m2)))

#two number input to divide
d1 = input("First number you would like to divide: ")
d2 = input("Second number you would like to divide: ")
print(divide(int(d1), int(d2)))

#two number input to subtract
s1 = input("First number you would like to subtract: ")
s2 = input("Second number you would like to subtract: ")
print(subtract(int(s1), int(s2)))

#three number input to find volume 
v1 = input("Length of the cube: ")
v2 = input("Width of the cube: ")
v3 = input("Height of the cube: ")
print(volumeOfCube(int(v1), int(v2), int(v3)))

#three number input to find volume 
a1 = input("First number you would like to find average: ")
a2 = input("Second number you would like to average: ")
a3 = input("Third number you would like to average: ")
print(average(int(a1), int(a2), int(a3)))

