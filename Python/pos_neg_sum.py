# In this program we are taking a list of numerical elements and 
# then we are dividing the list into two groups positive and negative using filter()
# and then we are calculating the sum of both groups using reduce()

import functools
#  Taking input of list element
print("Enter numerical element sep by Space: ")

lst = [int(v) for v in input().split()]
print("Given list={}".format(lst))

# Dividing the list into two groups positive and negative using filter()
poslst = list(filter(lambda v:v>0,lst))
neglst = list(filter(lambda v:v<0,lst))

print("Positive list={}".format(poslst))
print("Negative list={}".format(neglst))

# Calculating the sum of both groups using reduce()
posSum = functools.reduce(lambda x,y:x+y ,poslst)
negSum = functools.reduce(lambda x,y:x+y ,neglst)

print("Positive sum={}".format(posSum))
print("Negative sum={}".format(negSum))
