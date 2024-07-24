from get_disease import get_disease

def chatbot():
    """
    Function to interact with the user and provide disease information based on symptoms.
    """
    print("Welcome to the Healthcare Chatbot!")
    while True:
        # Get user input
        user_input = input("Enter your symptom (or type 'exit' to quit): ").strip()
        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Thank you for using the Healthcare Chatbot. Stay healthy!")
            break
        # Get disease based on the symptom
        disease = get_disease(user_input)
        # Display the result
        print(f"Based on your symptom, you might have: {disease}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
