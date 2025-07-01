# Clinical Reports to EMR Converter 🏥📄➡️📊

This project automates the extraction of key medical terms from unstructured clinical reports (e.g., pathology, histopathology) and maps them into structured EMR data formats.

## 🔬 Objective

To help match patients with clinical trials by:
- Extracting NER-based medical entities using BioBERT
- Cleaning & processing raw clinical text
- Merging features with metadata (like histo types, IDs, etc.)
- Outputting structured data for integration with EMR/FHIR formats

## 📁 Project Structure

```
clinicalreports_to_emr/
├── main.py                          # Entry point for the pipeline
├── process_merged_reports.py        # Merges extracted features into structured format
├── merge_reports_with_metadata.py   # Combines clinical reports with histopathological metadata
├── fix_filenames.py                 # Ensures consistent file naming conventions
├── histo_metadata.csv               # Metadata file containing patient/clinical info
├── features_full/                   # Directory containing extracted clinical features
└── ner/
    ├── ner_model.py                 # NER pipeline using BioBERT
    └── cleaner.py                   # Preprocessing and text cleaning for reports
```



## 🔧 Tech Stack

- Python 🐍
- BioBERT (via HuggingFace Transformers)
- pandas, os, regex
- Git & GitHub for version control

## 📦 Future Work

- Add FHIR integration
- Automate report ingestion from PDF
- LangChain for querying patient data

## 👨‍💻 Author

Abhishek Kokadwar, IIITM Gwalior  
GitHub: [Abhishek86798](https://github.com/Abhishek86798)

