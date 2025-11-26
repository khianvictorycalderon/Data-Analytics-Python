import numpy as np
import matplotlib.pyplot as plt

# Sample data
people = {
    "Mark": 0,
    "Sean": 1,
    "Dishiela": 2,
    "Azil": 3,
    "Jayvee": 4
}

days = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4
}

# We'll use this in plotting
day_number = np.array([1, 2, 3, 4, 5])

# Allowace in one week
allowance = np.array([
    # Day 1 - 5, Mon - Friday
    [200, 400, 150, 300, 600],
    [400, 200, 300, 350, 150],
    [250, 300, 100, 200, 300],
    [150, 200, 350, 400, 550],
    [300, 250, 150, 200, 350]
])

# Get Mark allowance on Thursday
print(f"Mark's allowance on Thursday is: {allowance[people['Mark']][days['Thursday']]}")

# Get Azil's allowance on Tuesday
print(f"Azil's allowance on Tuesday is: {allowance[people['Azil']][days['Tuesday']]}")

# Get Sean's allownace in One Week
print(f"Sean's allowance in one week are: {allowance[people['Sean']]}")

# Let's start plotting
plt.figure(figsize=(10,6))

# Let's put label first
plt.xticks(day_number, list(days.keys()))
plt.xlabel("Days of the Week")
plt.ylabel("Allowances")

# Plot all people
for name, idx in people.items():
    plt.plot(day_number, allowance[idx], marker="o", label=name)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Person")
plt.show()