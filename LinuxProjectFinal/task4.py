from task2 import *
from datetime import *

totalDays = 0
totalrb = 0
flag = 0


def numOfDays(getSD, getED):
    global totalDays

    SD = datetime.strptime(str(getSD).strip(), '%d %B %Y')
    ED = datetime.strptime(str(getED).strip(), '%d %B %Y')

    spaceSD = re.split('\s+', str(SD))
    spaceED = re.split('\s+', str(ED))

    rSD = re.split(r'-', str(spaceSD[0]))
    rED = re.split(r'-', str(spaceED[0]))

    SD_date = date(int(rSD[0]), int(rSD[1]), int(rSD[2]))
    ED_date = date(int(rED[0]), int(rED[1]), int(rED[2]))
    delta = ED_date - SD_date

    totalDays += int(delta.days)
    return totalDays


def totalRB(getRB):
    global totalrb
    totalrb += int(getRB)


def avCar(cl):
    global totalrb, totalDays, flag
    for i in range(0, len(rentalCompleted)):
        if cl == rentalCompleted[i].get("CL"):
            flag = 1
            getSD = rentalCompleted[i].get("SD")
            getED = rentalCompleted[i].get("ED")
            getRB = rentalCompleted[i].get("RB")
            numOfDays(getSD, getED)
            totalRB(getRB)
            continue

        if flag == 0 and i == len(rentalCompleted) - 1:
            print("The car does not exist")
    return totalrb / totalDays
