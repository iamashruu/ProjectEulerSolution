#Multiples of 3 and 5 below 1000
result=0
num=1000
for nums in range(1,num):
    if (nums%3==0) or (nums%5==0):
        result+=nums


print(result)
#Shortway:
print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))