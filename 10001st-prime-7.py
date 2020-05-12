#import time and math modules
import time, math

#Time at the start of execution
start = time.time()

#Function to check if the number is prime or not
def isPrime(n):
 if (n+1)%6 == 0 or (n-1)%6 == 0:
  for i in range(2, int(round(math.sqrt(n)+1))):
   if n%i == 0:
    return False
  return True
 return False

#Counter for counting the prime numbers
#We took it equal to 2 because
#we are starting with 4 and have already counted 2,3
counter = 2

#Numbers starting from 4
i = 4

#Assuming the nth-prime to be 0
prime = 0

#Starting a for loop
while counter < 10001:
 if isPrime(i):
  counter = counter+1
  prime = i
  i = i+1
 i = i+1

#Printing the output
print(str(counter)+' prime is '+str(prime))

#Time at the end of execution
end = time.time()

#Printing the time of execution
print(end-start)

#Fastest Way:

#sieve of Erotosthenes
#One of the best algorithm to generate prime numbers
def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(math.sqrt(n)+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

#Prime number we have to find
nth_prime = 10001

#Maximum value that the prime number can take
#According to http://math.stackexchange.com/a/1259/137013
upper_bound = nth_prime*math.log(nth_prime) + nth_prime*math.log(math.log(nth_prime))

#Printing the prime number
print(sieve(int(upper_bound))[10000])