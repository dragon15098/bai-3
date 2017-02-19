clothe = ["T-Shirt", "Sweater"]
while True:
    a = input("Welcome. What do you want(C,R,U,D)").lower()
    if (a=="c"):
        clothe.append(input("New item?"))
        print("Our items:", end=' ')
        for i in range(len(clothe)-1):
            print(clothe[i], end=', ')
        print(clothe[(len(clothe))-1])
    elif (a=="r"):
        print("Our items:", end=' ')
        for i in range(len(clothe)-1):
            print(clothe[i], end=', ')
        print(clothe[len(clothe)-1])
    elif (a=="d"):
        position = int(input("Delete position? "))
        clothe.pop(position)
        print("Our items:", end=' ')
        for i in range(len(clothe)-1):
            print(clothe[i], end=', ')
        print(clothe[len(clothe)-1])
    elif (a=="u"):
        position = int(input("Update position? "))
        new_clothe = input("New item? ")
        clothe[position] = new_clothe
        print("Our items:", end=' ')
        for i in range(len(clothe)-1):
            print(clothe[i], end=', ')
        print(clothe[len(clothe)-1])
    print()
