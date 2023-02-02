a1 = int(input())
a2 = int(input())
a3 = int(input())
aSum = a1 + a2 + a3
grade = ''
if  0 <= aSum <= 49:
    grade = 'F'
elif  50 <= aSum <= 54:
    grade = 'D'
elif  55 <= aSum <= 59:
    grade = 'D+'
elif  60 <= aSum <= 64:
    grade = 'C'
elif  65 <= aSum <= 69:
    grade = 'C+'
elif  70 <= aSum <= 74:
    grade = 'B'
elif  75 <= aSum <= 79:
    grade = 'B+'
elif  80 <= aSum <= 100:
    grade = 'A'
print(grade)