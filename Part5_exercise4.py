

# part 5 , exercise 4: + Who's your grandaddy?

choice = None
fathers = {"John": "Josh", "Josh": "Manny", "Andrew": "Michael", "Michael": "Robert", "Barney": "Bob", "Bob": "Manuel",
          "Jake": "Dylan", "Dylan": "Dominic", "Manny": "William", "Max": "Bill"}

while choice != "0":
    print("""
	0 - Quit
	1 - Find out who's your father
	2 - Add a pair
	3 - Delete a pair
	4 - Replace a pair
	5 - Get a grandfather
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
        son1 = input("\nWhats the son's name? ").capitalize()
        if son1 in fathers:
            print("\nWho's ", son1, "'s father? It's: ", fathers[son1], sep='')
        else:
            print("\nI don't know who your father is :(")

    # add a pair
    elif choice == "2":
        addaFather = input("What is the name of the father? ")
        addaSon = input("What is the name of the son? ").capitalize()
        fathers.update({addaSon: addaFather})
        print("\nYou added ", addaFather, " as the father of ", addaSon, "!", sep='')

    # delete a pair
    elif choice == "3":
        deletePair = input("Who would you like to delete, write down \
         the name of the son and the pair will be deleted: ").capitalize()
        if deletePair in fathers:
            del fathers[deletePair]
            print("\n You deleted", deletePair, "and his father.")
        else:
            print("\nThat person doesnt exist! Try adding him.")

    # replace a father
    elif choice == "4":
        pick = input("Which father-son pair do you want to redefine?: ").capitalize()
        if pick in fathers:
            father = input("Who is the new father?: ").capitalize()
            fathers[pick] = father
            print("\n", pick, "has a new father.")
        else:
            print("I don't know who you are talking about...")
    # unknown choice
    elif choice == "5":
        son = input("Whose grandfather would you like to check?: ").capitalize()

        father_check = False
        grandad_check = False

        for x, y in fathers.items():
            if son == x:
                print(f"{y} is the Father of {son}")
                father_check = True
                dad = y
        if father_check == False:
            print("No father found.")
        if father_check:
            for x, y in fathers.items():
                if dad == x:
                    print(f"{y} is the Grandfather of {son}")
                    grandad_check = True
        if grandad_check == False:
            print("No Grandfather found.")
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")
