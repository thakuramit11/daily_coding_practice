# Function to calculate the sum of squares of elements 
# at indices that are divisors of the array length of 1-indexed array
def sumOfSquares(nums):
  n = len(nums)
  total = 0
  for i in range(n):  
    if n%(i+1)==0:
        total+=nums[i]**2  
  return total    

nums = [1,2,3,4,5,6,7,8,9,10]
print(sumOfSquares(nums))