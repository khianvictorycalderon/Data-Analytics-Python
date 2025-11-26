import pandas as pd

# From a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 17, 22],
    "City": ["Manila", "Lucena", "Tayabas"]
}

df = pd.DataFrame(data)
print(df) # Like microsoft excel's data

# # Sample reading/saving a .csv or .xlsx file
# # CSV
# csv_data = pd.read_csv("data.csv")
# csv_data.to_csv("filename.csv", index=False)
# # Excel
# excel_data = pd.read_excel("data.xlsx")
# excel_data.to_excel("filename.xlsx", index=False)

# ------------------------------------------------
# SELECTING DATA

# # Single column
# ages = df["Age"]

# # Multiple columns
# subset = df[["Name", "City"]]

# # Rows by index
# row_0 = df.iloc[0]

# # Rows by condition
# adults = df[df["Age"] > 25]

# ------------------------------------------------
# MODIFYING DATA

# # Add new column
# df["Salary"] = [50000, 60000, 70000]

# # Modify values
# df["Age"] = df["Age"] + 1

# # Drop column
# df = df.drop("Salary", axis=1)

# ------------------------------------------------
# HANDLING MISSING DATA

# df.dropna(inplace=True)             # Drop rows with NaN
# df.fillna(0, inplace=True)          # Fill NaN with 0
# df["Age"].fillna(df["Age"].mean())  # Fill NaN with mean

# ------------------------------------------------
# SORTING DATA

# df.sort_values(by="Age", ascending=False)