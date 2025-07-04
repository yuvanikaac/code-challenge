'''
GET A THREE DIGIT NUMBER FROM THE USER AND THEM AND GIVE THE SUM
'''
num=int(input("Enter the three digit number:"))
result=(num//100)+((num//10)%10)+(num%10)
print("The sum of the three digit number is:",result)
