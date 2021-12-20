# Asaad Halayqa 1172102
# Yousef Ghanem 1172333


import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4

t1.readFile()
t2.fillList()


def callMenu():
    print("Press enter to continue")
    input()
    print("\n" * 10)
    menu()


def inqury():
    option = input("\nDo you want info About cars (c) OR a person (p)\n\tTo return to Main menu (m):\n")

    if option == 'c':
        cl = input("Enter the car license number(CL) :")
        t2.car(str(cl))
        callMenu()

    elif option == 'p':
        choose = input("Do you want to enter Name (n) or id (i):")
        if choose == 'n':
            name = input("Enter Name:")
            for i in range(len(t2.rentalCompleted)):
                if t2.rentalCompleted[i].get('Name') == name:
                    t2.person(t2.rentalCompleted[i].get('Id'))
            callMenu()

        elif choose == 'i':
            id = input("Enter ID:")
            t2.person(id)
            callMenu()
        else:
            print("invalid input!")
            callMenu()
    elif option == 'm':
        print("\n" * 10)
        menu()
    else:
        print("invalid input!")
        callMenu()


print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to Rental Car Company\n")


def menu():
    print("  Main Menu: ")
    print("\t 1. Inquiry about car or a person.")
    print("\t 2. Rent a car.")
    print("\t 3. Information about specific car.")
    print("\t 4. Print summary of missing and recovered data.")
    print("\t 5. Exit.")
    choice = input("\nEnter your choice: \n")

    if choice == '1':
        inqury()
    elif choice == '2':
        startDate1 = input("Start date (xx-xx-xxxx):\n")
        endDate1 = input("End date (xx-xx-xxxx):\n")
        t3.rent(startDate1, endDate1)
        callMenu()
    elif choice == '3':
        for i in range(0, len(t4.rentalCompleted)):
            print("CL: " + t4.rentalCompleted[i].get("CL") + ", CM: " + t4.rentalCompleted[i].get("CM") + ", Year: " +
                  t4.rentalCompleted[i].get("Year"))

        cl = input("\nEnter the CL of the desired car:")
        t4.avCar(cl)
        print("Number of days the car was rented: " + str(t4.totalDays))
        print("Revenue made by renting the car: " + str(t4.totalrb))
        print("Average price per day for renting each car: " + str(t4.totalrb / t4.totalDays))
        callMenu()

    elif choice == '4':
        print()
        t1.printSummary()
        callMenu()

    elif choice == '5':
        exit(0)
    else:
        print("Invalid choice")
        callMenu()


menu()
