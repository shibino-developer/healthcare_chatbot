import spacy
import joblib
from symptom_disease import symptom_disease_map

# Load NLP model and ML model
nlp = spacy.load('en_core_web_sm')
model = joblib.load('disease_predictor.pkl')

def preprocess_text(text):
    """
    Preprocess text to extract meaningful tokens.
    """
    doc = nlp(text.lower().strip())
    lemmatized_text = " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
    print(f"Original text: '{text}' -> Preprocessed text: '{lemmatized_text}'")
    return lemmatized_text

def get_disease(symptom):
    """
    Function to get the disease based on the symptom with NLP processing and ML model.
    """
    # Preprocess the symptom text
    processed_symptom = preprocess_text(symptom)
    
    # Predict the disease using the ML model
    try:
        predicted_disease = model.predict([processed_symptom])[0]
        print(f"Predicted disease from model: '{predicted_disease}'")
    except Exception as e:
        print(f"Error predicting disease: {e}")
        predicted_disease = "Unknown symptom. Please consult a doctor."
    
    return predicted_disease
