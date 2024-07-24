from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import joblib

# Load data
data = pd.read_csv('symptoms_diseases.csv')

# Features and labels
X = data['Symptom']
y = data['Disease']

# Split data for evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model pipeline with TF-IDF and SVM
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer(ngram_range=(1, 3), max_features=2000)),  # Use trigrams and more features
    ('classifier', SVC(kernel='linear'))  # Use SVM with linear kernel
])

# Train the model on the full training set
pipeline.fit(X_train, y_train)

# Predict and evaluate on test data
y_pred = pipeline.predict(X_test)
print("Model evaluation report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred, labels=pipeline.classes_)
conf_matrix_df = pd.DataFrame(conf_matrix, index=pipeline.classes_, columns=pipeline.classes_)
print("Confusion Matrix:")
print(conf_matrix_df)

# Save the trained model
joblib.dump(pipeline, 'disease_predictor_svm.pkl')
