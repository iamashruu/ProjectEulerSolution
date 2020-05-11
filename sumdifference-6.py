#Sum square difference-06
import time

#Time at the start of execution
start = time.time()
def square_of_sum(number):
    result=0
    for num in range(1,number+1):
        result+=num
    return result**2

def sum_of_square(number):
    result=0
    for num in range(1,number+1):
        result+=num**2
    return result

#Difference
print(square_of_sum(100)-sum_of_square(100))

#Time at the end of execution
end = time.time()

#printing the execution time
print(end-start)

#Another Way:
start = time.time()
#sum of squares of natural numbers
sum1 = sum(map(lambda x: x**2, range(1,101)))

#square of sum of natural numbers
sum2 = sum(range(1,101))**2

#result
result = sum2 - sum1

#printing the result
print(result)
#Time at the end of execution
end = time.time()

#printing the execution time
print(end-start)

#Another Way
start_time= time.time()
sum1 = 0

#sum2 variable to store the value of
#Sum of natural numbers
sum2 = 0

#For loop to iterate through the numbers from
# 1 - 100
for i in range(1,101):
	sum1 = sum1 + i*i
	sum2 = sum2 + i

#Required answer is
# square of sum of numbers - sum of squares of numbers
result = sum2**2 - sum1

#Printing the numbers
print("The result is %d"%result)

#Time at the end of execution
end_time = time.time()

#Total time taken
total_time = end_time - start_time

#Printing out the execution time
print('Executed in '),
print(end_time - start_time)

#Another Way=> Fastest

start_time= time.time()
n=100
squareSum = 0
sumSquare = ((n * (n+1))/2) ** 2

squareSum = ((2*n)+1)*(n+1)*n//6

num = sumSquare - squareSum
print(num)


end_time = time.time()

#Total time taken
total_time = end_time - start_time

#Printing out the execution time
print('Executed in '),
print(end_time - start_time)