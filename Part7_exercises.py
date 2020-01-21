#with open('helloworld.txt') as f:
#    for line in f:
#        print(line, end='')

with open('helloworld.txt', 'w') as f:
    f.write("This is a test la lala \n and this is the second line")

with open('helloworld.txt') as f:
    with open('emptyfile.txt', 'w') as f1:
        for line in f:
            f1.write(line)