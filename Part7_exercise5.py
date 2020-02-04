try:
    txt = 'abc'.upper()
    print(txt)
except AttributeError:
   print("abc does not have attribute 'upper'")

try:
   'abc'.convert()
except AttributeError:
   print("abc does not have attribute 'convert'")
