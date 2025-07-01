import pandas as pd

df = pd.read_csv("merged_metadata.csv")

# Replace .txt.hstlgy with .txt
df["filename"] = df["filename"].str.replace(".txt.hstlgy", ".txt")

df.to_csv("merged_metadata.csv", index=False)
print("✅ Fixed filenames saved.")
