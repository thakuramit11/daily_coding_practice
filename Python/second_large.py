''' In this code we are finding the second largest number in a list of numbers.
 If the list has less than two elements, it returns None. It first finds the maximum number in the list,
 then iterates through the list again to find the second largest number that is less than the maximum.
 If no second largest number is found, it returns None.'''
def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for a second largest
    
    max = numbers[0]
    second_max = float('-inf')
    
    for n in numbers:
        if n>max:
            max = n
    for n in numbers:            
        if n<max and n>second_max:
            second_max = n 
    if second_max == 0:
        second_max = None  # No second largest found        
    return second_max

print(second_largest([-5, -2, -8]))  # Output: -5 
print(second_largest([1, 2, 3, 4, 5]))  # Output: 4
print(second_largest([10]))  # Output: None
print(second_largest([5, 5, 5]))  # Output: None