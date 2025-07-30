'''GET A TWO DIGIT NUMBER FROM THE USER AND CHECK IF THE DIGIT 0 IS GREATER THAN DIGIT 1.IF YES PRINT 1 OTHERWISE PRINT 0'''
num=int(input("Enter a number:"))
if((num%10)>((num//10)%10)):
    print("1")
else:
    print("0")
