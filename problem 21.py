'''GET A FOUR DIGIT NUMBER FROM THE USER AND REVERSE ONLY THE LAST TWO DIGITS OF THE NUMBER AND RETURN IT'''
num=int(input("Enter a four digit number:"))
f=num//100
l=num%100
rev=(l%10)*10+(l//10)
result=f*100+rev
print(result)
