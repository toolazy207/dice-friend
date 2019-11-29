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
                typeOfDie = int(negStringSplit[0])
                negStringSplit[0] = "0"
                for num in negStringSplit:
                    mod += (int(num) * (-1))
                break
            break

        elif "+" in mess[1]:
            while modIncrement == 0:
                posString = mess[1]
                modIncrement += 1
                posStringSplit = posString.split("+")
                typeOfDie = int(posStringSplit[0])
                posStringSplit[0] = "0"
                for num in posStringSplit:
                    mod += int(num)
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


def dicemax(message):
    mess = message.split("d")
    maxmess = mess[1].split("k")
    dieType = maxmess[0]
    modIncrement = 0
    mod = 0
    diceRollStr = "Rolls: "
    maxRollStr = "Max Rolls: "
    maxList = []
    resultStr = "Results: "
    if mess[0] == "":
        timesDice = 1
    else:
        timesDice = int(mess[0])
    while "+" or "-" in maxmess[1]:
        if "+" in maxmess[1]:
            while modIncrement == 0:
                maxmessPlus = maxmess[-1].split("+")
                maxmessMod = int(maxmessPlus[0])
                maxmessPlus[0] = "0"
                for num in maxmessPlus:
                    mod += int(num)
                modIncrement += 1
                break
            break

        elif "-" in maxmess[1]:
            while modIncrement == 0:
                maxmessMinus = maxmess[-1].split("-")
                maxmessMod = int(maxmessMinus[0])
                maxmessMinus[0] = "0"
                for num in maxmessMinus:
                    mod -= int(num)
                modIncrement += 1
                break
            break

        else:
            maxmessMod = int(maxmess[-1])
            break

    modString = ("Mod: " + str(mod))

    while timesDice != 0:
        diceRoll = random.randint(1, int(dieType))

        if timesDice != 1:
            diceRoll = random.randint(1, int(dieType))
            maxList.append(str(diceRoll))
            diceRollStr += (str(diceRoll) + ", ")
        else:
            maxList.append(str(diceRoll))
            diceRollStr += str(diceRoll)
        timesDice -= 1
    print(maxList)
    maxRollList = []
    while maxmessMod != 0:
        maxRoll = max(maxList, key=lambda x: int(x))
        if maxmessMod == 1:
            maxRollStr += str(maxRoll)
            maxRollList.append(str(maxRoll))
        else:
            maxRollStr += (str(maxRoll) + ", ")
            maxRollList.append(str(maxRoll))
        maxList.remove(max(maxList, key=lambda x: int(x)))
        maxmessMod -= 1
    if mod != 0:
        print(maxRollList)
        for number in maxRollList:
            resultStr += (str(int(number) + mod) + ", ")

    else:
        pass
    if resultStr.endswith(", "):
        resultStr = resultStr[:-2]
    if mod == 0:
        return modString, diceRollStr, maxRollStr
    else:
        return modString, diceRollStr, maxRollStr, resultStr


