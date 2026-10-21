
from functools import reduce

employees = {
    "Aman": {"salary": 25000, "score": 85},
    "Riya": {"salary": 30000, "score": 65},
    "Karan": {"salary": 20000, "score": 75},
    "Neha": {"salary": 40000, "score": 90},
    "Rohit": {"salary": 18000, "score": 55}
}

# 1. Classify employee performance
def performance_level(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    else:
        return "Needs Improvement"

# 2. Select employees with a score of at least 70
eligible = list(
    filter(lambda emp: emp[1]["score"] >= 70, employees.items())
)

# 3. Calculate revised salaries with a 10% hike
revised = list(
    map(
        lambda emp: {
            "name": emp[0],
            "score": emp[1]["score"],
            "salary": emp[1]["salary"] * 1.10,
            "hike": emp[1]["salary"] * 0.10
        },
        eligible
    )
)

# 4. Sort by revised salary, highest first
revised.sort(key=lambda emp: emp["salary"], reverse=True)

# 5. Calculate total revised salary expense
total_salary = reduce(
    lambda total, emp: total + emp["salary"],
    revised,
    0
)

# 6. Calculate total hike budget
total_hike = reduce(
    lambda total, emp: total + emp["hike"],
    revised,
    0
)

# 7. Display results
print("Employee Performance Report")

for emp in revised:
    level = performance_level(emp["score"])
    print(
        f'{emp["name"]}: Salary = ₹{emp["salary"]:.0f}, '
        f'Hike = ₹{emp["hike"]:.0f}, Performance = {level}'
    )

print("\nHighest-paid eligible employee:", revised[0]["name"])
print("Total revised salary expense: ₹", total_salary)
print("Total hike budget: ₹", total_hike)
