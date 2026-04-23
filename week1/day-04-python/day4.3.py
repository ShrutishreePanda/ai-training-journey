import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, None, 78, 90]
}

df = pd.DataFrame(data)

df["Marks"].fillna(df["Marks"].mean(), inplace=True)

filtered = df[df["Marks"] > 80]

print(filtered)