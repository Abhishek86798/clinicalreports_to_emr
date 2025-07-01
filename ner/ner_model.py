from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

import torch

device = 0 if torch.cuda.is_available() else -1
print(f"Device set to use {'GPU' if device == 0 else 'CPU'}")

def load_biobert_ner_pipeline():
    model_name = "d4data/biomedical-ner-all"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    
    nlp_ner = pipeline(
    "ner",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple",
    device=device  # 👈 this enables GPU if available
)

    return nlp_ner

def extract_entities(text, nlp_pipeline):
    return nlp_pipeline(text)
