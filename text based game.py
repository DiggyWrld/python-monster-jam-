import random
def monster():
    num = random.ranrange (1,100)
    if num <30:
        print("mummy")
    if num >30:
        print("vampire")
room = 1
print("Welcome to the scary haunted house!")
while True:
    if room == 1:
        print("You are in room 1. You can go 'n' or 'e'.")
        choice = input()
        if choice ==  'e':
            room = 2
        elif choice == 'n':
            room = 4
        else:
            print("not an option, dummy")
    if room == 2:
        print("You are in room 2. You can go 'n' or 'w'")
        choice = input()
        if choice == 'w':
            room = 1
        elif choice == 'n':
            room = 3
        else:
            print("Not an option my boy ")
    if room == 3:
        print(" You are in room 3. You can go 'w' or 's'")
        choice = input()
        if choice ==  'w':
             room = 4
        elif choice == 'n':
             room = 2
        else:
            print("Not a option my boy")
    if room == 4:
        print(" You are in room 4. You can go 'w' or s'")
        choice = input()
        if choice == 'w':
            room = 5
        elif choice == 's':
            room = 2
        else:
            print("Not a option my boy")
    if room == 5:
        print(" You are in room 5. You can go 'e'")
        choice = input()
        if choice == 'e':
            room = 4
        else:
            print("Not a option my boy")
