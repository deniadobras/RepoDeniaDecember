father = {
    "John" : "Josh",
    "Andrew" : "Michael",
    "Barney": "Bob",
    "Jake" : "Dylan"
}

print(father["Jake"])

father["Max"] = "Bill"
del father["Andrew"]

print(father)

inputName = str(input("Enter a name: "))
print(father[inputName])