
import functools

employees = [
    {"name": "Aman", "salary": 25000, "score": 85},
    {"name": "Riya", "salary": 30000, "score": 65},
    {"name": "Karan", "salary": 20000, "score": 75},
    {"name": "Neha", "salary": 40000, "score": 90},
    {"name": "Rohit", "salary": 18000, "score": 55}
]

# 1. Filter eligible employees
eligible = list(filter(
    lambda e: e["score"] >= 70, employees
))

# 2. Give eligible employees a 10% hike
hiked = list(map(
    lambda e: {
        **e,
        "new_salary": e["salary"] * 1.10
    },
    eligible
))

# 3. Calculate total revised salary
total_salary = functools.reduce(
    lambda total, e: total + e["new_salary"],
    hiked,
    0
)

# 4. Sort by revised salary (highest first)
hiked.sort(
    key=lambda e: e["new_salary"],
    reverse=True
)

# 5. Display results
for e in hiked:
    print(
        e["name"],
        "| Score:", e["score"],
        "| Revised salary:", e["new_salary"]
    )

print("Total revised salary:", total_salary)
