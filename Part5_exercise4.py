

# part 5 , exercise 4:  Who's your grandaddy?


father = {"John": "Josh", "Josh": "Manny", "Andrew": "Michael", "Michael": "Robert", "Barney": "Bob", "Bob": "Manuel",
          "Jake": "Dylan", "Dylan": "Dominc", "Manny": "William", "Max": "Bill"}

son = input("Whose grandfather would you like to check?: ")

father_check = False
grandad_check = False

for x, y in father.items():
    if son == x:
        print(f"{y} is the Father of {son}")
        father_check = True
        dad = y
if father_check == False:
    print("No father found.")
if father_check:
    for x, y in father.items():
        if dad == x:
            print(f"{y} is the Grandfather of {son}")
            grandad_check = True
if grandad_check == False:
    print("No Grandfather found.")
