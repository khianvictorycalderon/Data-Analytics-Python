import pandas as pd

# From a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 17, 22],
    "City": ["Manila", "Lucena", "Tayabas"]
}

df = pd.DataFrame(data)
print(df) # Like microsoft excel's data