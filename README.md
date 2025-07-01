# Clinical Reports to EMR Converter 🏥📄➡️📊

This project automates the extraction of key medical terms from unstructured clinical reports (e.g., pathology, histopathology) and maps them into structured EMR data formats.

## 🔬 Objective

To help match patients with clinical trials by:
- Extracting NER-based medical entities using BioBERT
- Cleaning & processing raw clinical text
- Merging features with metadata (like histo types, IDs, etc.)
- Outputting structured data for integration with EMR/FHIR formats

## 📁 Project Structure

clinicalreports_to_emr/
├── main.py # Entry point
├── process_merged_reports.py # Merges extracted features
├── merge_reports_with_metadata.py # Combines reports with CSV metadata
├── fix_filenames.py # Renames files for consistency
├── histo_metadata.csv # Metadata file (e.g., patient info)
├── features_full/ # Extracted features from reports
├── ner/
│ ├── ner_model.py # BioBERT-based model
│ └── cleaner.py # Preprocessing and cleaning


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

