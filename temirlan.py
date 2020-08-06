num1 = int(input("Enter num1")) 
num2 = int(input("Enter num2"))

if num1 < num2:
    print(num1)
elif num1 > num2:
    print(num2)
elif num1 == num2:
    print(num1, "==", num2)
else:
    print('else')



num1 = int(input('Enter num1'))
num2 = int(input('Enter num2'))
num3 = int(input('Enter num3'))

if num2 <= num1 and num3 <= num1:
    print(num1)
elif num1 <= num2 and num3 <= num2:
    print(num2)
elif num1 <= num3 and num2 <= num3:
    print(num3)
else:
    print ('else')