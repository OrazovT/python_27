"""
условные операторы
if условие:
    body
    ....
elif условие:
    body
    ....
elif условие:
    body
    ....
elif условие:
    body
    ....
elif условие:
    body
    ....
elif условие:
    body
    ....
else:
    body




Сравнительные операторы
>, <, ==, <=, >=, !=

Логические операторы
not, is, in, and, or, xor


"""

if 20 < 10:
    print("First if")

elif 1==1:
    print("Elif first")

elif 2==2:
    print("Elif second")

else:
    print("Else")


if 20 == 20 and 10 != 10:
    print("IF AND")
elif 10 > 80 or 4 > 2:
    print("IF OR")
else:
    print("Else")
    

num1 = 40
num2 = 10
num3 = 50

nummax = -1

if num1 > nummax:
    nummax = num1


if num2 > nummax:
    nummax = num2


if num3 > nummax:
    nummax = num3

num222 = 50

if num222 % 2 == 0:
    print("even")
else:
    print("odd")