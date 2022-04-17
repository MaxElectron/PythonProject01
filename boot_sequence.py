import time
import os


def newGame():
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
    return name
