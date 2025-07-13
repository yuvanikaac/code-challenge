'''
GET A NUMBER FROM THE USER SUBTRACT 5 FROM THAT NUMBER IF THE  SUM OF THE NUMBER  IS ODD ,THEN PRINT THE RESULT.DO NOT USE 'if'
'''
num = int(input("Enter a number:"))
result=num-5*(((num//10)+(num%10))%2)
print(result)
