import joblib

# Load the trained model
model = joblib.load('disease_predictor.pkl')

def get_disease(symptom):
    return model.predict([symptom])[0]

# Define test cases
test_cases = [
    ('fever', 'gastroenteritis'),
    ('headache', 'migraine'),
]

for symptom, expected_disease in test_cases:
    result = get_disease(symptom)
    assert result == expected_disease, f"Failed for '{symptom}': expected '{expected_disease}', got '{result}'"
    print(f"Symptom: {symptom} -> Disease: {result}")

print("All tests passed!")
