print("Welcome to Basic Chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").strip().lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user == "what is your name":
        print("Bot: My name is Basic Chatbot.")

    elif user == "good morning":
        print("Bot: Good Morning!")

    elif user == "good evening":
        print("Bot: Good Evening!")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")