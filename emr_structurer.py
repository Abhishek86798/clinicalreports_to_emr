def structure_emr_data(ner_results):
    print("\n📄 Structuring data into EMR format...\n")

    emr = {
        "Patient_Age": None,
        "Gender": None,
        "Procedure": [],
        "Symptoms": [],
        "Findings": "",
        "Diagnosis": "",
        "Medications": [],
        "Report_Date": None,
    }

    last_med = None

    for ent in ner_results:
        label = ent.get("entity", ent.get("entity_group", "UNKNOWN"))
        word = ent["word"]
        if label == "Age":
            emr["Patient_Age"] = word

        elif label == "History":
            if "male" in word.lower():
              emr["Gender"] = "Male"
            elif "female" in word.lower():
              emr["Gender"] = "Female"
            elif word.lower() in ["gender", "sex"]:
              # Could use an external rule to infer gender later
              emr["Gender"] = "Unknown"

        elif label == "Diagnostic_procedure":
            emr["Procedure"].append(word)

        elif label == "Sign_symptom":
            emr["Symptoms"].append(word)

        elif label in ["Detailed_description", "Biological_structure", "Area", "Lab_value"]:
            emr["Findings"] += word + " "

        elif label == "Disease_disorder":
            emr["Diagnosis"] += word + " "

        elif label == "Medication":
            if word.lower() == "medications":
               continue
            last_med = {"name": word, "dosage": ""}
            emr["Medications"].append(last_med)

        elif label == "Dosage" and last_med is not None:
            if last_med["dosage"]:
                last_med["dosage"] += " " + word
            else:
                last_med["dosage"] = word

        elif label == "Date":
            emr["Report_Date"] = word

    # Join procedure if list
    emr["Procedure"] = " ".join(emr["Procedure"]).strip()
    emr["Diagnosis"] = emr["Diagnosis"].strip()
    emr["Findings"] = emr["Findings"].strip()

    return emr
