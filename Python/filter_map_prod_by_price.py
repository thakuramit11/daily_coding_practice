# In this code, we have a list of products with their names and prices.
# We want to extract the names of products that have a price greater than 1000.
# using filter and map functions to achieve this.

products = [
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1200},
    {"name": "Monitor", "price": 8000},
    {"name": "USB", "price": 300},
    {"name": "Headphones", "price": 1500}
]

above_1000 =list(filter(lambda v:v['price']>1000,products))
prod_1000 = list(map(lambda v:v['name'],above_1000))
print(prod_1000)
