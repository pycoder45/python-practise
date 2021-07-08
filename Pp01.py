# 5.Write A Python program to find the reverse number of the given number 

num = 38337478
reverse_num = 0

while num != 0: 
  digit = num%10
  reverse_num = reverse_num*10 + digit
  num//=10
  
print("Reversed Number : ",reverse_num)

# 6.Write A python program to check whether the number is prime or not 

num = 28
check_p = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            check_p = True
            break
if check_p:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
  
# 8.Write A Python Program to print 1st 10 odd and even Number.

print(" Even \t\t Odd ")

for i in range(0,20): 
  if i%2 == 0: 
    print(i,"\t\t ")
  else : 
    print(i)
# Write A python program to find greatest and smallest number of given 3 Number 
num1 = 45
num2 = 87
num3 = 23

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

if (num1 <= num2) and (num1 <= num3):
   smallest = num1
elif (num2 <= num1) and (num2 <= num3):
   smallest = num2
else:
   smallest = num1

print("The largest number is", smallest)