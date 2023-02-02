import math
n = input()
x = n.split(" ")
m = int(x[0])
n = int(x[1])
arr1 = []
arr2 = []
ans = []
for i in range(m):
    members = [i for i in input().split()]
    arr1.append(members)
for i in range(m):
    members = [i for i in input().split()]
    arr2.append(members)
for i in range(m):
    temp = []
    for j in range(n):
        temp.append( int(arr1[i][j]) + int(arr2[i][j]) )
    ans.append(temp)
    
for k in ans:
    for j in k:
        print(j, end=" ")
    print("")