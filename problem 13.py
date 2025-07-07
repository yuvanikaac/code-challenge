'''
GET A FOUR DIGIT NUMBER FROM USER AND REVERSE ONLY THE FIRST TWO DIGITS AND RETURN THE RESULT
'''
num=int(input("Enter a four digit number:"))
f=num//100
l=num%100
rev=(f%10)*10+(f//10)
result=rev*100+l
print(result)

