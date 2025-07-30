'''GET A TWO DIGIT NUMBER FROM THE USER AND CHECK IF THE DIGIT1 IS LESS THAN OR EQUAL TO THE DIGIT 0.IF YES PRINT 1 OTHERWISE PRINT 0'''
num=int(input("Enter a two digit number:"))
if(((num//10)%10)<=(num%10)):
    print("1")
else:
    print("0")
