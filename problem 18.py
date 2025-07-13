'''
GET A NUMBER FROM THE USER SUBTRACT 5 FROM THAT NUMBER IF THE NUMBER'S TEN'S POSITION IS ODD ,THEN PRINT THE RESULT.DO NOT USE 'if'
'''
num = int(input("Enter a number:"))
result=num-5*((num//10)%2)
print(result)
