import statistics as st

baseDict = {}

def fileRead():
    fileTab = open("Base.txt", "r")

    for i in fileTab:
      lineTab = i.replace("\n", "").replace(',', '.').split("\t")
      baseDict[lineTab[0]] = [lineTab[1], lineTab[2], lineTab[3], lineTab[4], lineTab[5]]

    fileTab.close()

def fileWrite(dict, fileName):
    openFile = open(fileName, "w")
    for i in dict:
        openFile.write(i + "\t")
        for j in range(0, len(dict[i])):
            if j == len(dict[i]) - 1:
                openFile.write(str(dict[i][j]) + "\n")
            else:
                openFile.write(str(dict[i][j]) + "\t")
    openFile.close()

def replaceChoice (keyLine, modeReplace):
    numArray = list()
    for i in baseDict:
        if i == "":
            continue
        if baseDict[i][keyLine] == "N/A":
            continue
        numArray.append(float(baseDict[i][keyLine]))

    if modeReplace == "sa":
        return st.fmean(numArray)
    elif modeReplace == "mode":
        return st.mode(numArray)
    elif modeReplace == "med":
        return st.median(numArray)
    else:
        return 0

def normalize ():
    hightOfDict = len(baseDict[''])
    numArray = list()
    count = 0

    while count < hightOfDict:
        for i in baseDict:
            if i == '':
                continue
            if baseDict[i][count] == "N/A":
                continue
            numArray.append(float(baseDict[i][count]))

        for i in baseDict:
            if i == '':
                continue
            if baseDict[i][count] == "N/A":
                continue
            else:
                baseDict[i][count] = str((float(baseDict[i][count]) - min(numArray)) / (max(numArray) - min(numArray)))
        count += 1

def lengthVector (array1, array2, indexElem):
    sum = 0

    for i in range(0, len(array1)):
        if i == indexElem:
            continue
        if array1[i] == "N/A":
            continue

        sum += abs(float(array1[i]) - float(array2[i]))

    return sum

def manhattanMetric (dict, indexElem, keyLine):
    check = True
    while check:
        for i in dict:
            if i == keyLine:
                continue
            elif i == '':
                continue
            elif 'N/A' in dict[i]:
                continue
            else:
                minElem = i
                check = False

    for i in dict:
        if i == keyLine:
            continue
        elif i == '':
            continue
        elif 'N/A' in dict[i]:
            continue
        elif lengthVector(dict[keyLine], dict[i], indexElem) < lengthVector(dict[keyLine], dict[minElem], indexElem):
            minElem = i

    return dict[minElem][indexElem]

fileRead()

for i in baseDict:
    check = True

    while check:
        if "N/A" in baseDict[i]:
            baseDict[i][baseDict[i].index("N/A")] = replaceChoice(baseDict[i].index("N/A"), "sa")
        else:
            check = False

fileWrite(baseDict, "TabSA.txt")

fileRead()

for i in baseDict:
    check = True

    while check:
        if "N/A" in baseDict[i]:
            baseDict[i][baseDict[i].index("N/A")] = replaceChoice(baseDict[i].index("N/A"), "mode")
        else:
            check = False

fileWrite(baseDict, "TabMODA.txt")

fileRead()

for i in baseDict:
    check = True

    while check:
        if "N/A" in baseDict[i]:
            baseDict[i][baseDict[i].index("N/A")] = replaceChoice(baseDict[i].index("N/A"), "med")
        else:
            check = False

fileWrite(baseDict, "TabMD.txt")

fileRead()

normalize()

fileWrite(baseDict, "TabNORM.txt")

for i in baseDict:
    if i == '':
        continue

    check = True

    while check:
        if "N/A" in baseDict[i]:
            baseDict[i][baseDict[i].index("N/A")] = manhattanMetric(baseDict, baseDict[i].index("N/A"), i)
        else:
            check = False

fileWrite(baseDict, "TabMETRIC.txt")
