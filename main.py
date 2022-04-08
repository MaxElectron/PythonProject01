import os
import time

fileExists = os.path.isfile("save_data.txt")


def recalc(value, initial):
    return max(value - int((time.time() - initial) // 300), 0)


def load():
    if fileExists:
        file = open("save_data.txt", "r")
        state = file.read()
        file.close()
    else:
        state = "new_game"
    return state


def update():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("  ^~^  ,")
    print(" ('Y') )   Hunger:    ", end=' ')
    print(recalc(hungerLast, hungerTime))
    print(" /   \\/    Happiness: ", end=' ')
    print(recalc(happinessLast, happinessTime))
    print("(\\|||/)    Tiredness: ", end=' ')
    print(recalc(tirednessLast, tirednessTime))
    print("________   Experience:", end=' ')
    print(experienceLast)
    print("\n")


def save():
    open('save_data.txt', 'w').close()
    file = open("save_data.txt", "w")
    file.write(str(name))
    file.write("_")
    file.write(str(hungerLast))
    file.write("_")
    file.write(str(happinessLast))
    file.write("_")
    file.write(str(tirednessLast))
    file.write("_")
    file.write(str(experienceLast))
    file.write("_")
    file.write(str(hungerTime))
    file.write("_")
    file.write(str(happinessTime))
    file.write("_")
    file.write(str(tirednessTime))
    file.write("_")
    file.write(str(experienceTime))
    file.close()


# boot up
saveState = load()
flag = False

# pre game loop
if saveState == "new_game":  # if no save files found
    print("Welcome to \"VirtualPet_2.11\"!")
    print("Let's summon your friend...\n")
    print("---Press ENTER to continue---\n")
    input()
    # joke segment
    print("Initializing_Summon:  0%")
    time.sleep(0.7)
    print("Initializing_Summon: 10%")
    time.sleep(0.5)
    print("Initializing_Summon: 20%")
    time.sleep(0.1)
    print("Initializing_Summon: 30%")
    time.sleep(0.1)
    print("Initializing_Summon: 40%")
    time.sleep(0.1)
    print("Initializing_Summon: 50%")
    time.sleep(0.2)
    print("Initializing_Summon: 60%")
    time.sleep(0.1)
    print("Initializing_Summon: 70%")
    time.sleep(0.1)
    print("Initializing_Summon: 80%")
    time.sleep(0.2)
    print("Initializing_Summon: 90%")
    time.sleep(0.4)
    print("Initializing_Summon:100%")
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Summon successful, please name your pet...")
    name = input()
    while "_" in name:
        print("Name is not suitable, please enter a name without \'_\'")
        name = input()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Thanks for your time, take good care of {} :)\n If you need any help please type \"Help\"".format(name))
    print("---Press ENTER to continue---\n")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    hungerLast = 100
    happinessLast = 50
    tirednessLast = 100
    experienceLast = 0
    hungerTime = time.time()
    happinessTime = time.time()
    tirednessTime = time.time()
    experienceTime = time.time()
else:
    data = saveState.split('_')
    name = data[0]
    hungerLast = int(data[1])
    happinessLast = int(data[2])
    tirednessLast = int(data[3])
    experienceLast = int(data[4])
    hungerTime = float(data[5])
    happinessTime = float(data[6])
    tirednessTime = float(data[7])
    experienceTime = float(data[8])

# game loop
while not flag:

    update()

    save()

    command = input().lower()

    if command == "end":
        flag = True

    elif command == "help":
        print("Help:")
        print("Help - View all commands")
        print("End - Exit the game")
        print("Feed - Feed the pet")
        print("Train - Boost exp")
        print("Sleep - Give pet a break")
        print("Play - Entertain the pet\n")
        print("---Press ENTER to continue---\n")
        input()

    elif command == "feed":
        hungerLast = min(recalc(hungerLast, hungerTime) + 40, 100)
        hungerTime = time.time()
        tirednessLast -= 3

    elif command == "sleep":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("  ^~^  ,")
        print(" (>Y<) )   Hunger:    ", end=' ')
        print(recalc(hungerLast, hungerTime))
        print(" /   \\/    Happiness: ", end=' ')
        print(recalc(happinessLast, happinessTime))
        print("(\\|||/)    Tiredness: ", end=' ')
        print(recalc(tirednessLast, tirednessTime))
        print("Zzzzzzzz   Experience:", end=' ')
        print(experienceLast)
        print("\n")
        time.sleep(5)
        tirednessLast = min(recalc(tirednessLast, tirednessTime) + 40, 100)
        tirednessTime = time.time()
        hungerLast -= 3

    elif command == "train":
        if recalc(hungerLast, hungerTime) < 10:
            print("{} is too hungry".format(name))
            print("---Press ENTER to continue---\n")
            input()
            continue
        if recalc(tirednessLast, tirednessTime) < 10:
            print("{} is too tired".format(name))
            print("---Press ENTER to continue---\n")
            input()
            continue
        if recalc(happinessLast, happinessTime) < 10:
            print("{} is too sad".format(name))
            print("---Press ENTER to continue---\n")
            input()
            continue
        experienceLast += 1
        experienceLast *= 1.1
        experienceLast = int(experienceLast)
        hungerLast -= 5
        tirednessLast -= 5
        happinessLast -= 10

    elif command == "play":
        if recalc(hungerLast, hungerTime) < 10:
            print("{} is too hungry".format(name))
            print("---Press ENTER to continue---\n")
            input()
            continue
        if recalc(tirednessLast, tirednessTime) < 10:
            print("{} is too tired".format(name))
            print("---Press ENTER to continue---\n")
            input()
            continue
        os.system('cls' if os.name == 'nt' else 'clear')
        print("  ^~^  ,")
        print(" (^Y^) )   Hunger:    ", end=' ')
        print(recalc(hungerLast, hungerTime))
        print(" /   \\/    Happiness: ", end=' ')
        print(recalc(happinessLast, happinessTime))
        print("(\\|||/)    Tiredness: ", end=' ')
        print(recalc(tirednessLast, tirednessTime))
        print("Purrrrrr   Experience:", end=' ')
        print(experienceLast)
        print("\n")
        time.sleep(2)
        happinessLast = min(recalc(happinessLast, happinessTime) + 20, 100)
        happinessTime = time.time()
        hungerLast -= 10
        tirednessLast -= 6

    else:
        print("Type \"Help\" for help")
        print("---Press ENTER to continue---\n")
        input()
