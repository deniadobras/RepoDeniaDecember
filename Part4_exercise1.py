# Numbers divisible by 7 and multiple of 5

numbers=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        numbers.append(str(x))
print("Numbers divisible by 7 and multiple of 5 are: ", ', '.join(numbers))

#example given by Lore
# def mul_div():
#     z = list(range(1500,2701))
#     for n in list(range(1500,2701)):
#          if n%7 == 0 and n%5 == 0:
#             print((n))
#
# mul_div()