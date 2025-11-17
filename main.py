from bot.nlp import detect_intent, get_sentiment
from bot.commands import (
    handle_time,
    handle_weather,
    handle_smalltalk,
    handle_goodbye,
)
from bot.notes import add_note, get_notes

def main():
    print("🤖 Enhanced AI Chat Bot started. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        intent = detect_intent(user_input)
        sentiment = get_sentiment(user_input)

        # Emotion-aware greetings
        if intent == "greeting":
            if sentiment == "positive":
                print("Bot: Hey! Great to see you 😊")
            else:
                print("Bot: Hello. How can I assist you today?")

        elif intent == "goodbye":
            print("Bot:", handle_goodbye())

        elif intent == "smalltalk":
            print("Bot:", handle_smalltalk())

        elif intent == "time":
            print("Bot:", handle_time())

        elif intent == "weather":
            print("Bot:", handle_weather())

        elif intent == "add_note":
            add_note(user_input)
            print("Bot: Note saved!")

        elif intent == "show_notes":
            notes = get_notes()
            if not notes:
                print("Bot: You have no notes yet.")
            else:
                print("Bot: Here are your notes:")
                for n in notes:
                    print("-", n)

        else:
            # fallback for unknown intent
            if sentiment == "negative":
                print("Bot: I'm sorry you're feeling that way. Want to talk about it?")
            else:
                print("Bot: Hmm, I’m not sure I understand — but I’m learning!")

if __name__ == "__main__":
    main()
