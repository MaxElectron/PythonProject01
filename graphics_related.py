import time
import os


def recalc(value, initial):
    return max(value - int((time.time() - initial) // 300), 0)


def update(hungerlast, hungertime, happinesslast, happinesstime, tirednesslast, tirednesstime, experiencelast, switch):
    print("  ^~^  ,")
    if switch == "def":
        print(" ('Y') )   Hunger:    ", end=' ')
    elif switch == "sleep":
        print(" (>Y<) )   Hunger:    ", end=' ')
    else:
        print(" (^Y^) )   Hunger:    ", end=' ')
    print(recalc(hungerlast, hungertime))
    print(" /   \\/    Happiness: ", end=' ')
    print(recalc(happinesslast, happinesstime))
    print("(\\|||/)    Tiredness: ", end=' ')
    print(recalc(tirednesslast, tirednesstime))
    if switch == "def":
        print("________   Experience:", end=' ')
    elif switch == "sleep":
        print("Zzzzzzzz   Experience:", end=' ')
    else:
        print("Purrrrrr   Experience:", end=' ')
    print(experiencelast)
    print("\n")


def showHelp():
    print("Help:")
    print("Help - View all commands")
    print("End - Exit the game")
    print("Feed - Feed the pet")
    print("Train - Boost exp")
    print("Sleep - Give pet a break")
    print("Play - Entertain the pet\n")
    print("---Press ENTER to continue---\n")
    input()


def inappropriateCommand():
    print("Type \"Help\" for help")
    print("---Press ENTER to continue---\n")
    input()


def errorMsg(name, switch):
    print("{} is too {}".format(name, switch))
    print("---Press ENTER to continue---\n")
    input()
