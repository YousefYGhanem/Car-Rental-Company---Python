import re

fo = open("CarRentalCompleted.txt", "r")
rentalCompleted = []


def fillList():
    for line in fo.readlines():
        list = re.split(r';', line)
        rentalCompleted.append(
            {'Name': list[0], 'Id': list[1], 'Dob': list[2], 'Mobile': list[3], 'CL': list[4], 'CM': list[5],
             'Year': list[6], 'SD': list[7], 'ED': list[8], 'RB': list[9]})


def person(id):
    print("\nRecent records :")
    paid = 0
    co = 0
    for i in range(len(rentalCompleted)):
        if rentalCompleted[i].get('Id') == str(id):
            print(
                "CL: " + str(rentalCompleted[i].get('CL')) + ", CM: " + str(rentalCompleted[i].get('CM')) + ", Year: " +
                str(rentalCompleted[i].get('Year')) + ", SD: " + str(rentalCompleted[i].get('SD')) + ", ED: " + str(
                    rentalCompleted[
                        i].get('ED')) + ", RB: " + str(rentalCompleted[i].get('RB')))
            paid += int(rentalCompleted[i].get('RB'))
            co = i

    if rentalCompleted[co].get('Id') == str(id):
        print("Info about the person :")
        print("Name: " + rentalCompleted[co].get("Name"))
        print("ID: " + rentalCompleted[co].get('Id'))
        print("Date of birth: " + rentalCompleted[co].get('Dob'))
        print("Mobile number: " + rentalCompleted[co].get('Mobile'))
        print("Total money paid by person is : " + str(paid))
    else:
        print("No info about this person!")


def car(cl):
    print("\nRecent records :")
    revenue = 0
    co = 0
    for i in range(len(rentalCompleted)):
        if rentalCompleted[i].get('CL') == cl:
            print("Name: " + str(rentalCompleted[i].get("Name")) + ", Id: " + str(
                rentalCompleted[i].get("Id")) + ", Dob:" +
                  str(rentalCompleted[i].get("Dob")) + ", Mobile: " + str(rentalCompleted[i].get("Mobile")) + ", SD: " +
                  str(rentalCompleted[i].get("SD")) + ", ED: " + str(rentalCompleted[i].get("ED")) + ", RB: " + str(
                rentalCompleted[
                    i].get("RB")))
            revenue += int(rentalCompleted[i].get('RB'))
            co = i

    print("Info about the car :")
    print("Car license: " + str(rentalCompleted[co].get('CL')))
    print("Car make: " + str(rentalCompleted[co].get('CM')))
    print("Year of manufacturing the car:" + str(rentalCompleted[co].get('Year')))
    print("Total revenue for car is : " + str(revenue))
