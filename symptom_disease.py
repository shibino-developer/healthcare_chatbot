# symptom_disease.py

symptom_disease_map = {
    'fever': 'gastroenteritis',
    'headache': 'migraine',
    'chest pain': 'heart disease',
    'nausea': 'gastroenteritis',
    'fatigue': 'anemia',
    'rash': 'allergy',
    'vomiting': 'gastroenteritis',
    'stomach ache': 'gastroenteritis',
    'dizziness': 'vertigo',
    'sore throat': 'pharyngitis',
}

def get_disease(symptom):
    symptom_disease_map = {
        'fever': 'gastroenteritis',
        'headache': 'migraine',
        'rash': 'allergy',
        # Add more mappings as needed
    }
    # Return the disease or a default message if the symptom is unknown
    return symptom_disease_map.get(symptom, 'Unknown symptom. Please consult a doctor.')

# Test the function
if __name__ == "__main__":
    test_symptoms = ['fever', 'headache', 'rash', 'unknown symptom']
    for symptom in test_symptoms:
        print(f"Symptom: {symptom} -> Disease: {get_disease(symptom)}")
