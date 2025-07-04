'''
GET A TWO DIGIT NUMBER FROM USER AND PRINT THE REVERSE OF THE NUMBER
'''
num=int(input("Enter the number:"))
r=0
while num>0:
    n=num%10
    r=r*10+n
    num=num//10

print(r)
