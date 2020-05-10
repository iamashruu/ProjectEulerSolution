import time

#Time at the start of program
start_time = time.time()

#More Efficient 

#gcd function for calculating lcm
def gcd(n1,n2):
    if n1==0:
        return n2
    return gcd(n2%n1,n1)
    
    """
	remainder = 1
	while remainder != 0:
		remainder = n1%n2
		n1 = n2
		n2 = remainder
	return n1
    """

#lcm of two numbers using euclid Algorithm
#lcm = (number1*number2)/GCD(number1,number2)
def lcm(n1,n2):
	return (n1*n2)/gcd(n1,n2)

#lcm of 2,3
#You can also use (2*3)/gcd(2,3)
l = lcm(2,3)
#lcm of three numbers n1,n2,n3 is
#lcm(lcm(n1,n2),n3)
for i in range(4,21):
	l = lcm(l,i)

#Printing the lcm at the end
print(l)

#time at the end of program
end_time = time.time()

#total Time taken
print(end_time - start_time)

"""
#ShortWay
check = range(10,21)
a = 2520
b = False

while b == False:
   # if a % 2520 == 0:
        if all(a % n ==0 for n in check):
            b = True
        else:
            a = a + 2520
    #else:
       #  a = a + 1 

print(a)

#Another Way:

#Not Efficient

def ifDividesAll(num):
  for i in range(2,21):
    if num % i != 0:
      return False
  return True

num = 20
while True:
  if ifDividesAll(num):
    break
  else:
    num = num + 1
print(num)
"""

