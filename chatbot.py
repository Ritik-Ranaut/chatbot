from merge_sort import sort
import binary_search
import kmp_matcher

def load_responses():
    """Loads responses from file and sorts them."""
    try:
        with open("responses.txt", "r") as file:
            responses = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Error: responses.txt file not found!")
        return []
    
    # Sort responses using Merge Sort
    responses = sort(responses)
    return responses

def get_response(user_input, responses):
    """Finds the best chatbot response using pattern matching and binary search."""
    # First, use KMP pattern matching
    for response in responses:
        if kmp_matcher.kmp_search(user_input.lower(), response.lower()):
            return response

    # If no exact match, use binary search for closest match
    index = binary_search.binary_search(responses, user_input)
    return responses[index] if index != -1 else "Sorry, I don't understand that."

def main():
    """Runs the chatbot interaction loop."""
    responses = load_responses()
    if not responses:
        return

    print("Chatbot: Hello! Type your message (type 'exit' to stop).")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input, responses)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
