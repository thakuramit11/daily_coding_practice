# Program to check if a number is an Armstrong number or not
# Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
n = input("Enter a number: ")
sum = 0
for i in n:
    sum += int(i) ** len(n)
if sum == int(n): 
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
         
        