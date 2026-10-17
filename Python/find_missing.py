# Problem statement
# You're given a list containing distinct numbers from 1 to n, but exactly one number is missing.
# Write a function find_missing(nums, n) that returns the missing number.

def find_missing(nums, n):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    # Calculate the actual sum of the given list
    actual_sum = sum(nums)
    # The missing number is the difference between the expected and actual sums
    return expected_sum - actual_sum

lst = [1, 2, 3, 4, 6]  # Example list with a missing number
n = 6  # The maximum number in the range
print(find_missing(lst, n))  # Output: 5