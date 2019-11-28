import random


def dicebot(message):
    mess = message.split("d")
    mod = 0
    modIncrement = 0
    diceRollStr = ("Rolls: ")
    modStr = ("Mod: ")
    while "+" or "-" in mess:
        if "-" in mess[1]:
            while modIncrement == 0:
                negString = mess[1]
                modIncrement += 1
                negStringSplit = negString.split("-")
                negStringSplit[0] = "0"
                for num in negStringSplit:
                    mod += (int(num) * (-1))
                typeOfDie = int(mess[0])
                break
            break

        elif "+" in mess[1]:
            while modIncrement == 0:
                posString = mess[1]
                modIncrement += 1
                posStringSplit = posString.split("+")
                posStringSplit[0] = "0"
                for num in posStringSplit:
                    mod += int(num)
                typeOfDie = int(mess[0])
                break
            break
        else:
            typeOfDie = int(mess[1])
            break
    if mess[0] != "":
        timesDice = int(mess[0])
    else:
        timesDice = 1
    total = 0
    print("Mod: " + str(mod))
    print("Rolls: ", end="")
    while timesDice != 0:
        diceRoll = random.randint(1, typeOfDie)

        if timesDice != 1:
            diceRoll = random.randint(1, typeOfDie)
            total += diceRoll
            diceRollStr += (str(diceRoll) + ", ")
            print(str(diceRoll) + ", ", end="")
        else:
            total += diceRoll
            diceRollStr += str(diceRoll)
            print(str(diceRoll))

        timesDice -= 1

    total += mod
    resultString = ("Result: " + str(total))
    modStr += str(mod)
    return modStr, diceRollStr, resultString







