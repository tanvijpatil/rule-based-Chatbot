def chatbot_response(user_input):
    # Converting the user input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()

    # Rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but thanks for asking! How about you?"
    elif "your name" in user_input:
        return "I'm your friendly chatbot, here to help you with anything!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Happy to help."
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."
    elif "help" in user_input:
        return "I'm here to assist you. You can ask me about time, greetings, or anything else you have in mind!"
    elif "what can you do" in user_input:
        return "I can respond to greetings, tell the time, chat a bit, and help with basic queries!"
    elif "day" in user_input:
        from datetime import datetime
        today = datetime.now().strftime('%A')
        return f"Today is {today}."
    elif "ai" in user_input or "artificial intelligence" in user_input:
        return "Artificial Intelligence is a field of study that enables machines to learn and make decisions. It's fascinating!"
    elif "what's up" in user_input or "whats up" in user_input:
        return "Not much, just here to chat with you! How about you?"
    elif "your favorite color" in user_input:
        return "As a chatbot, I don't have preferences, but I think all colors are wonderful!"
    elif "i'm sad" in user_input or "feeling down" in user_input:
        return "I'm sorry to hear that. Remember, tough times don't last, but tough people do!"
    elif "i'm happy" in user_input or "feeling happy" in user_input:
        return "That's wonderful to hear! Keep spreading those positive vibes!"
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Main loop to interact with the chatbot
def chat():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'exit' or 'quit' to end the conversation.")
    
    while True:
        # Taking input from the user
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Generating and printing chatbot response
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
