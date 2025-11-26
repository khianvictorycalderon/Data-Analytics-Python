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