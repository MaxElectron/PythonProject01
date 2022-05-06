from boot_sequence import *
from graphics_related import *
from system_related import *

# boot up
saveState = load()
flag = False
# pre game loop
if saveState == "new_game":  # if no save files found - make a new pet
    name = newGame()
    hungerLast = 100
    happinessLast = 50
    tirednessLast = 100
    experienceLast = 0
    hungerTime = time.time()
    happinessTime = time.time()
    tirednessTime = time.time()
    experienceTime = time.time()
else:  # if any save files found - load up the pet
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
    os.system('cls' if os.name == 'nt' else 'clear')
    update(hungerLast, hungerTime, happinessLast, happinessTime, tirednessLast, tirednessTime, experienceLast, "def")
    save(name, hungerLast, happinessLast, tirednessLast, experienceLast,
         hungerTime, happinessTime, tirednessTime, experienceTime)
    command = input().lower()
    if command == "end":
        flag = True
    elif command == "help":
        showHelp()
    elif command == "feed":
        hungerLast = min(recalc(hungerLast, hungerTime) + 40, 100)
        hungerTime = time.time()
        tirednessLast -= 3
    elif command == "sleep":
        os.system('cls' if os.name == 'nt' else 'clear')
        update(hungerLast, hungerTime, happinessLast, happinessTime, tirednessLast, tirednessTime, experienceLast,
               "sleep")
        time.sleep(5)
        tirednessLast = min(recalc(tirednessLast, tirednessTime) + 40, 100)
        tirednessTime = time.time()
        hungerLast -= 3
    elif command == "train":
        if recalc(hungerLast, hungerTime) < 10:
            errorMsg(name, "hungry")
            continue
        if recalc(tirednessLast, tirednessTime) < 10:
            errorMsg(name, "tired")
            continue
        if recalc(happinessLast, happinessTime) < 10:
            errorMsg(name, "sad")
            continue
        experienceLast += 1
        experienceLast *= 1.1
        experienceLast = int(experienceLast)
        hungerLast -= 5
        tirednessLast -= 5
        happinessLast -= 10
    elif command == "play":
        if recalc(hungerLast, hungerTime) < 10:
            errorMsg(name, "hungry")
            continue
        if recalc(tirednessLast, tirednessTime) < 10:
            errorMsg(name, "tired")
            continue
        os.system('cls' if os.name == 'nt' else 'clear')
        update(hungerLast, hungerTime, happinessLast, happinessTime, tirednessLast, tirednessTime, experienceLast,
               "play")
        time.sleep(2)
        happinessLast = min(recalc(happinessLast, happinessTime) + 20, 100)
        happinessTime = time.time()
        hungerLast -= 10
        tirednessLast -= 6
    else:
        inappropriateCommand()
