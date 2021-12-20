from task4 import *


def rent(startDate1, endDate1):
    rSD = re.split(r'-', startDate1)
    rED = re.split(r'-', endDate1)

    startDate = datetime(int(rSD[2]), int(rSD[1]), int(rSD[0]))
    endDate = datetime(int(rED[2]), int(rED[1]), int(rED[0]))

    if endDate < startDate:
        print("The date entered wrong!")
        return

    rented = ['0']

    for i in range(0, len(rentalCompleted)):
        try:
            flag1 = 0
            SD = datetime.strptime(rentalCompleted[i].get("SD"), '%d %B %Y')
            ED = datetime.strptime(rentalCompleted[i].get("ED"), '%d %B %Y')

            if (startDate < SD and endDate < SD) or (startDate > ED and endDate > ED):
                for k in range(len(rented)):
                    if rentalCompleted[i].get("CL") == rented[k]:
                        flag1 = 1
                        continue

                if flag1 != 1:
                    print("CL: " + rentalCompleted[i].get("CL") + ", CM: " + rentalCompleted[i].get("CM") + ", Year: " +
                          rentalCompleted[i].get("Year"))
                    rented.append(rentalCompleted[i].get("CL"))

            else:
                rented.append(rentalCompleted[i].get("CL"))

        except ValueError:
            continue

    getCL = input("\nEnter the CL of the desired car: ")
    getCM = ""
    getYear = ""
    flag = 0
    for i in range(0, len(rentalCompleted)):
        if getCL == rentalCompleted[i].get("CL"):
            getCM = rentalCompleted[i].get("CM")
            getYear = rentalCompleted[i].get("Year")
            break
        if i == len(rentalCompleted) - 1:
            print("The car does not exist")
            flag = 1

    if flag == 0:
        getSD = startDate.strftime("%d %B %Y")
        getED = endDate.strftime("%d %B %Y")

        tDays = numOfDays(getSD, getED)
        avr = avCar(getCL)

        getRB = int(tDays * avr)

        print("Total cost is : " + str(getRB))
        ch = input("Do you agree with the cost? \n (y) for yes (n) for no\n")

        if ch == 'y':
            getName = input("Enter your name: ")
            getId = input("Enter your ID: ")
            getDob = input("Enter your date of birth (dd Month YYYY): ")
            getMobile = input("Enter your Mobile no.: ")

            rentalCompleted.append(
                {'Name': getName, 'Id': getId, 'Dob': getDob, 'Mobile': getMobile, 'CL': getCL, 'CM': getCM,
                 'Year': getYear, 'SD': getSD, 'ED': getED, 'RB': getRB})

            with open("CarRentalCompleted.txt", "a") as completed:
                completed.write("\n" +
                                str(getName) + ";" + str(getId) + ";" + str(
                    getDob) + ";" + str(getMobile) + ";" + str(
                    getCL) + ";" + str(getCM) + ";" + str(
                    getYear) + ";" +
                                str(getSD) + ";" + str(getED) + ";" + str(
                    getRB))

            with open("CarRentalOld.txt", "a") as old:
                old.write("\n" +
                          str(getName) + ";" + str(getId) + ";" + str(
                    getDob) + ";" + str(getMobile) + ";" + str(
                    getCL) + ";" + str(getCM) + ";" + str(
                    getYear) + ";" +
                          str(getSD) + ";" + str(getED) + ";" + str(
                    getRB))
