# In program  we are dividing the list into two groups 0-500 and 500-1000 Using filter() 
# and then we are giving hike of 10% using map() 
# to 0-500  and 20% to 500-1000 and then we are calculating the total salary of both groups using reduce() 

import functools
sallst = [int(v) for v in input("Enter list of employee salary btw 0 and 1001:").split() if 0<int(v)<1001]
print("-"*80)

sal_500 = list(filter(lambda v:v<501,sallst))
sal_1000 = list(filter(lambda v:500<v<1001,sallst))

print(sal_1000)
print(sal_500)

hike_500 = list(map(lambda v:v+v*0.1,sal_500))
hike_1000 = list(map(lambda v:v+v*0.2,sal_1000))

print(hike_1000)
print(hike_500)

total_500 = functools.reduce(lambda x,y:x+y,hike_500)
total_1000= functools.reduce(lambda x,y:x+y,hike_1000)

# Printing the results
print("-"*50)
for s,h in zip(sal_500,hike_500):
    print("\t{}\t\t{}".format(s,h))
print("-"*50)
print("\tTotal Salary:\t",total_500)

print("-"*50)
print("-"*50)
for s,h in zip(sal_1000,hike_1000):
    print("\t{}\t\t{}".format(s,h))
print("-"*50)
print("\tTotal Salary:\t",total_1000)