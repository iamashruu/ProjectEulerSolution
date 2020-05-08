#Largest prime factor

num=int(input("Enter the number:"))
n=2

#largest prime factor is smaller than squareroot of the number

while n*n<num:
    while num%n==0:
        num=num//n   
    n+=1
    
print(num)