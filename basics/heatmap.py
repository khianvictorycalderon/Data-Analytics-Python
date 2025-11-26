# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a small dataset of 5 people
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, 30, 22, 28, 35],
    "Height_cm": [165, 175, 180, 160, 170],
    "Weight_kg": [55, 70, 75, 50, 68],
    "Gender": ["Female", "Male", "Male", "Female", "Male"]
}

df = pd.DataFrame(data)
print(df)

# Set Seaborn style
sns.set_style("whitegrid")

# 1. Scatter plot: Height vs Weight
plt.figure(figsize=(8,5))
sns.scatterplot(x="Height_cm", y="Weight_kg", hue="Gender", style="Gender", s=100, data=df)
plt.title("Height vs Weight of 5 People")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()

# 2. Bar plot: Age of each person
plt.figure(figsize=(8,5))
sns.barplot(x="Name", y="Age", hue="Gender", data=df)
plt.title("Age of Each Person")
plt.show()

# 3. Box plot: Weight distribution by Gender
plt.figure(figsize=(8,5))
sns.boxplot(x="Gender", y="Weight_kg", data=df)
plt.title("Weight Distribution by Gender")
plt.show()

# 4. Pair plot: Visualize relationships between numeric variables
sns.pairplot(df, hue="Gender", height=2.5)
plt.show()

# 5. Heatmap: Correlation between numeric variables
plt.figure(figsize=(6,4))
corr = df[["Age", "Height_cm", "Weight_kg"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()