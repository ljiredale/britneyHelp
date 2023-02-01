alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
first = ['snake', 'legend', 'rebel', 'phantom', 'soldier' ,'deadly', 'midnight', 'dark' ,'invisible', 'gilded']
second = ['caster', 'whisper' ,'crush', 'shadow', 'dragon', 'dragon', 'viper', 'claw', 'blade', 'wolf', 'breath', 'moon' ,'demon']
print(len(alphabet))
def createName(first, last):
    retFirst = ""
    retLast = ""
    for i in range(4):
        if first[0] == alphabet(i):
            retFirst == 'snake'
    for i in range(5, 9):
        if first[0] == alphabet(i):
            retFirst == 'snake'
    for i in range(4):
        if first[0] == alphabet(i):
            retFirst == 'snake'
    for i in range(4):
        if first[0] == alphabet(i):
            retFirst == 'snake'
    for i in range(4):
        if first[0] == alphabet(i):
            retFirst == 'snake'
    


firstName = input("Input your first name: ")
lastName = input("Input your last name: ")

print(createName(firstName, lastName))