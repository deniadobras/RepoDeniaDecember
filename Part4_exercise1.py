# Numbers divisible by 7 and multiple of 5

numbers=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        numbers.append(str(x))
print("Numbers divisible by 7 and multiple of 5 are: ", ', '.join(numbers))
