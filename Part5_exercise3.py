# part 5 , exercise 3:  Who's your daddy?


# father = {"John": "Josh", "Josh": "Manny", "Andrew": "Michael", "Michael": "Robert", "Barney": "Bob", "Bob": "Manuel",
#           "Jake": "Dylan", "Dylan": "Dominic", "Manny": "William", "Max": "Bill"}
#
# inputNameFather = str(input("Enter a name: "))
#
# print(father[inputNameFather])

choice = None
fathers = {"John": "Josh", "Josh": "Manny", "Andrew": "Michael", "Michael": "Robert", "Barney": "Bob", "Bob": "Manuel",
           "Jake": "Dylan", "Dylan": "Dominic", "Manny": "William", "Max": "Bill"}

while choice != "0":
    print("""
	0 - Quit
	1 - Find out who's your father
	2 - Add a pair
	3 - Delete a pair
	""")
    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Goodbye.")

    # find out who's the father
    elif choice == "1":
        print("\nHere are all of your people you can currently find out who their father is:\n")
        for key in fathers:
            print(key)
        son1 = input("\nWhats the son's name? ")
        if son1 in fathers:
            print("\nWho's ", son1, "'s father? It's: ", fathers[son1], sep='')
        else:
            print("\nI don't know who your father is :(")

    # add a pair
    elif choice == "2":
        addaFather = input("What is the name of the father? ")
        addaSon = input("What is the name of the son? ")
        fathers.update({addaSon: addaFather})
        print("\nYou added ", addaFather, " as the father of ", addaSon, "!", sep='')

    # delete a pair
    elif choice == "3":
        deletePair = input(
            "Who would you like to delete, write down the name of the son and the pair will be deleted: ")
        if deletePair in fathers:
            del fathers[deletePair]
            print("\n You deleted ", deletePair, "and his father.")
        else:
            print("\nThat person doesnt exist! Try adding him.")

    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")
