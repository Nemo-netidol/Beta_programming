import math
n = input()
capital = False
small = False
for i in n:
    if i.isupper():
        capital = True
    elif i.islower():
        small = True
if capital and small:
    print("Mix")
if capital == True and small == False:
    print("All Capital Letter")
elif capital == False and small == True:
    print("All Small Letter")