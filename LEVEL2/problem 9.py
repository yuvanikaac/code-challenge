'''GET A TWO DIGIT NUMBER FROM THE USER AND CHECK IF THE DIGIT 0 IS LESS THAN THE DIGIT 1.IF YES PRINT 1 OTHERWISE PRINT 0'''
num=int(input("Enter a number:"))
a=num%10
b=(num//10)%10
if(a<b):
    print("1")
else:
    print("0")
