import os


fileExists = os.path.isfile("save_data.txt")


def load():
    if fileExists:
        file = open("save_data.txt", "r")
        state = file.read()
        file.close()
    else:
        state = "new_game"
    return state


def save(name, hungerlast, happinesslast, tirednesslast, experiencelast,
         hungertime, happinesstime, tirednesstime, experiencetime):
    open('save_data.txt', 'w').close()
    file = open("save_data.txt", "w")
    file.write(str(name))
    file.write("_")
    file.write(str(hungerlast))
    file.write("_")
    file.write(str(happinesslast))
    file.write("_")
    file.write(str(tirednesslast))
    file.write("_")
    file.write(str(experiencelast))
    file.write("_")
    file.write(str(hungertime))
    file.write("_")
    file.write(str(happinesstime))
    file.write("_")
    file.write(str(tirednesstime))
    file.write("_")
    file.write(str(experiencetime))
    file.close()
