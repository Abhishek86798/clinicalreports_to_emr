import pandas as pd
import os

# Paths
metadata_path = "histo_metadata.csv"
reports_folder = "features_full"

# Load metadata (tab-separated)
df = pd.read_csv(metadata_path, sep="\t")

# Ensure filename column exists
if "filename" not in df.columns:
    raise ValueError("❌ 'filename' column not found in metadata!")

# Add report_text column
df["report_text"] = None

# Fill report_text by reading corresponding .txt files
merged_count = 0

for idx, row in df.iterrows():
    raw_file_name = row["filename"]
    if isinstance(raw_file_name, str) and not raw_file_name.startswith("._"):
        clean_file_name = raw_file_name.strip().replace(".hstlgy", "")
        txt_path = os.path.join(reports_folder, clean_file_name)
        
        if os.path.exists(txt_path):
            try:
                with open(txt_path, "r", encoding="utf-8") as f:
                    df.at[idx, "report_text"] = f.read().strip()
                    merged_count += 1
            except Exception as e:
                print(f"⚠️ Error reading {clean_file_name}: {e}")
        else:
            print(f"❌ File not found: {clean_file_name}")

# Save the merged output
df.to_csv("merged_metadata.csv", index=False)
print(f"✅ Merged {merged_count} reports successfully into merged_metadata.csv")
