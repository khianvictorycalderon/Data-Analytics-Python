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

# Allowace in one week
allowance = np.array([
    # Day 1 - 5, Mon - Friday
    [200, 400, 150, 300, 600],
    [400, 200, 300, 350, 150],
    [250, 300, 100, 200, 300],
    [150, 200, 350, 400, 550],
    [300, 250, 150, 200, 350]
])