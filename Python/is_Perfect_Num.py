# sum of perfect divisors should be equal to n
def is_perfect_number():
    n=int(input("Enter a number to check:"))
    sum = 0
    for i in range(1,(n//2)+1):
         if n%i==0: # if i is a divisor of n
             sum+=i
    if sum==n:# if the sum of divisors is equal to n, then n is a perfect number
        return n,"is a perfect number"        
    else:     # if the sum of divisors is not equal to n, then n is not a perfect number
        return n,"is not a perfect number"        
 
print(is_perfect_number())
      
  