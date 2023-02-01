def helloWorld():
    print('Hello World')
def helloName(name):
    print("Hello " + name)
def printTimes(phrase, count):
    for i in range(count):
        print(phrase)
def squared(num):
    return num*num
def angularVelocity(m, r, v):
    return (m*v**2)/r
def printList(numlist):
    for i in range(len(numlist)):
        print(numlist[i])
helloWorld()
helloWorld()
printTimes("hello john", 3)
printTimes("hello anthony", 2)
print(squared(3))
print(squared(4))
print(angularVelocity(4, 5, 6))
print(angularVelocity(5,3,7))
printList([3, 4, 5, 6])
printList([7, 3, 5, 7])