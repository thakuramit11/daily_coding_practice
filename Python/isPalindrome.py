# Check if a word is a palindrome (case-insensitive)
# A palindrome is a word that reads the same backward as forward, ignoring case.
# special characters and spaces are considered in this implementation.

ispalin = lambda word:"Palindrome" if word.lower()==word.lower()[::-1] else "Not palindrome"
print(ispalin(input())) 
