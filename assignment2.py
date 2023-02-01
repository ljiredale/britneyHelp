first = ['snake', 'legend', 'rebel', 'phantom', 'soldier' ,'deadly', 'midnight', 'dark' ,'invisible', 'gilded']
second = ['caster', 'whisper' ,'crush', 'shadow', 'dragon', 'owl', 'viper', 'claw', 'blade', 'wolf']
def createName(first, last):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    retFirst = ""
    retLast = ""

    for i in range(2):
        if first[0] == alphabet[i]:
            retFirst = 'snake'
    for i in range(3,5):
        if first[0] == alphabet[i]:
            retFirst = 'legend'
    for i in range(4, 8):
        if first[0] == alphabet[i]:
            retFirst = 'rebel'
    for i in range(7,9):
        if first[0] == alphabet[i]:
            retFirst = 'phantom'
    for i in range(9, 12):
        if first[0] == alphabet[i]:
            retFirst = 'soldier'
    for i in range(12, 16):
        if first[0] == alphabet[i]:
            retFirst = 'deadly'
    for i in range(16, 19):
        if first[0] == alphabet[i]:
            retFirst = 'midnight'
    for i in range(19, 21):
        if first[0] == alphabet[i]:
            retFirst = 'dark'
    for i in range(21, 23):
        if first[0] == alphabet[i]:
            retFirst = 'invisible'
    for i in range(23, 26):
        if first[0] == alphabet[i]:
            retFirst = 'gilded'
    for i in range(2):
        if last[0] == alphabet[i]:
            retLast = 'caster'
    for i in range(3,5):
        if last[0] == alphabet[i]:
            retLast == 'whisper'
    for i in range(4, 7):
        if last[0] == alphabet[i]:
            retLast = 'crush'
    for i in range(7,9):
        if last[0] == alphabet[i]:
            retLast = 'shadow'
    for i in range(9, 12):
        if last[0] == alphabet[i]:
            retLast = 'dragon'
    for i in range(12, 16):
        if last[0] == alphabet[i]:
            retLast = 'owl'
    for i in range(16, 19):
        if last[0] == alphabet[i]:
            retLast = 'viper'
    for i in range(19, 21):
        if last[0] == alphabet[i]:
            retLast = 'claw'
    for i in range(21, 23):
        if last[0] == alphabet[i]:
            retLast = 'blade'
    for i in range(23, 26):
        if last[0] == alphabet[i]:
            retLast = 'wolf'
    return "Your name is " + retFirst + " " + retLast
    


firstName = input("Input your first name: ")
lastName = input("Input your last name: ")

print(createName(firstName, lastName))