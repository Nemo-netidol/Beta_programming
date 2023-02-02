import math
n = input()
x = n.split(" ")
ans = math.sqrt( ( float(x[0]) ** 2 ) + ( float(x[1]) ** 2) )  
print(f"{ans:.6f}")