def clean_ner_tokens(raw_entities):
    merged = []
    current_word = ""
    current_entity = ""
    current_score = 0.0

    for ent in raw_entities:
        word = ent["word"]
        label = ent.get("entity_group") or ent.get("entity", "UNKNOWN")
        score = ent.get("score", 0.0)

        if word.startswith("##"):
            current_word += word[2:]
            current_score = max(current_score, score)
        else:
            if current_word:
                if current_word.isalpha():  # optional: filter junk
                    merged.append({
                        "entity": current_entity,
                        "word": current_word,
                        "score": round(current_score, 3)
                    })
            current_word = word
            current_entity = label
            current_score = score

    # Append the last one
    if current_word and current_word.isalpha():
        merged.append({
            "entity": current_entity,
            "word": current_word,
            "score": round(current_score, 3)
        })

    return merged
