import re
import datetime

duplicate = 0
dateformat = 0
namedrop = 0
iddrop = 0
dopdrop = 0
mobiledrop = 0
nocomplete = 0
makedrop = 0
cariddrop = 0
caryeardrop = 0


def readFile():
    global duplicate, dateformat, namedrop, iddrop, dopdrop, mobiledrop, nocomplete, makedrop, cariddrop, caryeardrop

    fo = open("CarRentalOld.txt", "r")
    miss = open("CarRentalMissing.txt", "w")
    completed = open("CarRentalCompleted.txt", "w")

    rental = []
    for line in fo.readlines():
        listSplit = re.split(r';', line)

        try:
            rental.append(
                {'Name': listSplit[0], 'Id': listSplit[1], 'Dob': listSplit[2], 'Mobile': listSplit[3],
                 'CL': listSplit[4],
                 'CM': listSplit[5],
                 'Year': listSplit[6], 'SD': listSplit[7], 'ED': listSplit[8], 'RB': listSplit[9]})

        except IndexError:
            miss.write(line)

    flag = ""
    f = True
    for i in range(0, len(rental)):
        co = 0
        drop = 0

        if not rental[i].get('Name') and not rental[i].get('Id') and not rental[i].get('Mobile'):
            miss.write(
                str(rental[i].get('Name') + ";" + rental[i].get('Id') + ";" + rental[i].get('Dob') + ";" + rental[
                    i].get(
                    'Mobile') + ";" + rental[i].get('CL') + ";" + rental[i].get('CM') + ";" + rental[i].get(
                    'Year') + ";" +
                    rental[
                        i].get('SD') + ";" + rental[i].get('ED') + ";" + rental[i].get('RB')))
            nocomplete += 1
            drop = 3
            f = False

        else:
            if not rental[i].get('Name'):
                namedrop += 1
                for j in range(0, len(rental)):
                    if rental[i].get('Id') == rental[j].get('Id') and rental[j].get('Name'):
                        rental[i]['Name'] = rental[j].get('Name')
                        break


            try:
                Name = re.split('\s+', str(rental[i].get('Name')))

                rental[i]['Name'] = str(Name[0]).capitalize() + " " + str(Name[1]).capitalize()
            except IndexError:
                print(str(Name) + str(rental[i].get('Id')))

            if not rental[i].get('Id'):
                iddrop += 1
                for j in range(0, len(rental)):
                    if rental[i].get('Mobile') == rental[j].get('Mobile') and rental[j].get('Id'):
                        rental[i]['Id'] = rental[j].get('Id')
                        break

            if not rental[i].get('Mobile'):
                mobiledrop += 1
                for j in range(0, len(rental)):
                    if rental[i].get('Id') == rental[j].get('Id') and rental[j].get('Mobile'):
                        rental[i]['Mobile'] = rental[j].get('Mobile')
                        break

        if not rental[i].get('Dob'):
            dopdrop += 1
            if drop != 3:
                for j in range(0, len(rental)):
                    if rental[i].get('Id') == rental[j].get('Id') and rental[j].get('Dob'):
                        rental[i]['Dob'] = rental[j].get('Dob')
                        break

        if not rental[i].get('CM'):
            makedrop += 1
            for j in range(0, len(rental)):
                if rental[i].get('CL') == rental[j].get('CL') and rental[j].get('CM'):
                    rental[i]['CM'] = rental[j].get('CM')
                    break

        if not rental[i].get('Year'):
            caryeardrop += 1
            for j in range(0, len(rental)):
                if rental[i].get('CL') == rental[j].get('CL') and rental[j].get('Year'):
                    rental[i]['Year'] = rental[j].get('Year')
                    break

        if not rental[i].get('CL'):
            if drop != 3:
                miss.write(
                    str(rental[i].get('Name') + ";" + rental[i].get('Id') + ";" + rental[i].get('Dob') + ";" + rental[
                        i].get(
                        'Mobile') + ";" + rental[i].get('CL') + ";" + rental[i].get('CM') + ";" + rental[i].get(
                        'Year') + ";" +
                        rental[
                            i].get('SD') + ";" + rental[i].get('ED') + ";" + rental[i].get('RB')))
            f = False
            cariddrop += 1

        if not rental[i].get('SD') or not rental[i].get('ED') or not rental[i].get('RB'):
            if drop != 3:
                miss.write(
                    str(rental[i].get('Name') + ";" + rental[i].get('Id') + ";" + rental[i].get('Dob') + ";" + rental[
                        i].get(
                        'Mobile') + ";" + rental[i].get('CL') + ";" + rental[i].get('CM') + ";" + rental[i].get(
                        'Year') + ";" +
                        rental[
                            i].get('SD') + ";" + rental[i].get('ED') + ";" + rental[i].get('RB')))
            f = False

        r = re.compile('.*/.*/.*')
        r2 = re.compile('.*-.*-.*')

        if r.match(rental[i].get("Dob")):
            listDate = re.split(r'/', rental[i].get("Dob"))
            x = datetime.datetime(int(listDate[2]), int(listDate[1]), int(listDate[0]))
            rental[i]["Dob"] = x.strftime("%d %B %Y ")
            dateformat += 1

        elif r2.match(rental[i].get("Dob")):
            listDate = re.split(r'-', rental[i].get("Dob"))
            x = datetime.datetime(int(listDate[2]), int(listDate[1]), int(listDate[0]))
            rental[i]["Dob"] = x.strftime("%d %B %Y ")
            dateformat += 1

        if r.match(rental[i].get("SD")):
            listDate = re.split(r'/', rental[i].get("SD"))
            x = datetime.datetime(int(listDate[2]), int(listDate[1]), int(listDate[0]))
            rental[i]["SD"] = x.strftime("%d %B %Y ")
            dateformat += 1

        elif r2.match(rental[i].get("SD")):
            listDate = re.split(r'-', rental[i].get("SD"))
            x = datetime.datetime(int(listDate[2]), int(listDate[1]), int(listDate[0]))
            rental[i]["SD"] = x.strftime("%d %B %Y ")
            dateformat += 1

        if r.match(rental[i].get("ED")):
            listDate = re.split(r'/', rental[i].get("ED"))
            x = datetime.datetime(int(listDate[2]), int(listDate[1]), int(listDate[0]))
            rental[i]["ED"] = x.strftime("%d %B %Y ")
            dateformat += 1

        elif r2.match(rental[i].get("ED")):
            listDate = re.split(r'-', rental[i].get("ED"))
            x = datetime.datetime(int(listDate[2]), int(listDate[1]), int(listDate[0]))
            rental[i]["ED"] = x.strftime("%d %B %Y ")
            dateformat += 1
        flag = rental[i].get("Name")

        for n in range(0, i - 1):
            rental[i]["Name"] = rental[i]["Name"].lower()
            rental[n]["Name"] = rental[n]["Name"].lower()
            if rental[i] == rental[n]:
                co = 1
                break
        if co == 1:
            duplicate += 1
            continue
        rental[i]["Name"] = flag

        if f:
            completed.write(
                str(rental[i].get('Name') + ";" + rental[i].get('Id') + ";" + rental[i].get('Dob') + ";" + rental[
                    i].get(
                    'Mobile') + ";" + rental[i].get('CL') + ";" + rental[i].get('CM') + ";" + rental[i].get(
                    'Year') + ";" +
                    rental[
                        i].get('SD') + ";" + rental[i].get('ED') + ";" + rental[i].get('RB')))
    fo.close()
    miss.close()
    completed.close()


def printSummary():
    print("Summary of data missing in the database:")
    print("Number of duplicate enteries in the database = " + str(duplicate))
    print("Number of enteries with wrong date format in the database = " + str(dateformat))
    print("Number of enteries where names are dropped from the database = " + str(namedrop))
    print("Number of enteries where Ids are dropped from the database = " + str(iddrop))
    print("Number of enteries where dob are dropped from the database = " + str(dopdrop))
    print("Number of enteries where mobile are dropped from the database = " + str(mobiledrop))
    print("Number of enteries where personal entry can not be completed = " + str(nocomplete))
    print("Number of enteries where car make are dropped from the database = " + str(makedrop))
    print("Number of enteries where car Ids are dropped from the database = " + str(cariddrop))
    print("Number of enteries where car models (year) are dropped from the database = " + str(caryeardrop))
    print("\n")
    print("Summary of data recovered in the database:")
    print("Number of duplicate enteries removed from the new database = " + str(duplicate))
    print("Number of enteries with wrong date format fixed in the database = " + str(dateformat))
    print("Number of enteries where names are recovered from the database = " + str(namedrop))
    print("Number of enteries where Ids are recovered from the database = " + str(iddrop))
    print("Number of enteries where dob are recovered from the database = " + str(dopdrop))
    print("Number of enteries where mobile are recovered from the database = " + str(mobiledrop))
    print("Number of enteries where car make are recovered from the database = " + str(makedrop))
    print("Number of enteries where car models (year) are recovered from the database = " + str(caryeardrop))
    print("Done")
