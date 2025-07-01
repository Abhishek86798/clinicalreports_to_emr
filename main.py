from extract.pdf_reader import extract_text_from_pdf
from ner.ner_model import load_biobert_ner_pipeline, extract_entities
from ner.cleaner import clean_ner_tokens
from emr_structurer import structure_emr_data  # import the new function

def main():
    pdf_path = "data/sample_report.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    
    print("\n✅ Text Extracted.\n")
    
    # Load NER model
    print("🔍 Loading BioBERT model...")
    nlp = load_biobert_ner_pipeline()

   # Apply NER
    print("🧠 Running NER...\n")
    entities = extract_entities(extracted_text[:1000], nlp)  # use first 1000 chars for demo

    print("\n🔧 Cleaning and merging tokens...\n")
    cleaned_results = clean_ner_tokens(entities)

    for ent in cleaned_results:
        print(f"{ent['entity']} ➜ {ent['word']} (score: {ent['score']})")

    # Clean entities
    print("\n🔧 Cleaning and merging tokens...\n")
    cleaned_results = clean_ner_tokens(entities)

    # Show cleaned tokens
    for ent in cleaned_results:
        print(f"{ent['entity']} ➜ {ent['word']} (score: {ent['score']})")

    # Structure into EMR
    print("\n📄 Structuring data into EMR format...\n")
    emr = structure_emr_data(cleaned_results)

    import json
    print(json.dumps(emr, indent=2))

   

if __name__ == "__main__":
    main()


