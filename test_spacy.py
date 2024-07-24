import spacy

def test_spacy_installation():
    try:
        # Attempt to load spaCy model
        nlp = spacy.load('en_core_web_sm')
        print("spaCy and model loaded successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_spacy_installation()
