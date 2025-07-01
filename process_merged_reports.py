import pandas as pd
from ner.ner_model import load_biobert_ner_pipeline, extract_entities
from emr_structurer import structure_emr_data
from ner.cleaner import clean_ner_tokens

# Load data
df = pd.read_csv("merged_metadata.csv").head(10)

# Rename if needed
df = df.rename(columns=lambda x: x.strip())  # Strip spaces
df = df.rename(columns={"report_text": "report"})  # Rename to match code

# Drop rows with missing reports
df = df.dropna(subset=["report"])

# Load model
nlp_pipeline = load_biobert_ner_pipeline()

structured_emrs = []

for idx, row in df.iterrows():
    text = str(row["report"]).strip()  # Ensure it's a string
    if not text:
        continue  # Skip empty text

    site = row["site"]
    histology = row["histology"]
    filename = row.get("filename", "")

    # Step 1: Run NER
    ner_results = extract_entities(text, nlp_pipeline)

    # Step 2: Clean NER output
    cleaned_results = clean_ner_tokens(ner_results)

    # Step 3: Structure into EMR
    emr = structure_emr_data(cleaned_results)

    # Step 4: Add metadata
    emr["Site"] = site
    emr["Histology"] = histology
    emr["Source_File"] = filename

    # Step 5: Append
    structured_emrs.append(emr)


# Save result
import json
with open("structured_emrs.json", "w") as f:
    json.dump(structured_emrs, f, indent=2)

print("✅ All valid reports processed and saved to structured_emrs.json")
