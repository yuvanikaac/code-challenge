'''
GET A NUMBER FROM THE USER SUBTRACT 5 FROM THAT NUMBER IF THE ONE'S DIGIT NUMBER AND 100'S DIGIT NUMBER  IS ODD ,THEN PRINT THE RESULT.DO NOT USE 'if'
'''
num = int(input("Enter a number:"))
o=num%10
h=(num//100)%10
result=num-5*((o%2)*(h%2))
print(result)
