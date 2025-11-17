from datetime import datetime
import random

def handle_weather():
    return "I can't fetch API weather yet, but it's probably nice!"

def handle_time():
    return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

def handle_smalltalk():
    replies = [
        "I'm just a little bot, but I'm doing great 😄",
        "All systems running! What about you?",
        "Just thinking about algorithms and snacks.",
        "I'm here and ready to chat!",
        "Feeling electric today ⚡"
    ]
    return random.choice(replies)

def handle_goodbye():
    replies = [
        "Goodbye! Take care 👋",
        "See you soon!",
        "Bye bye! It was nice talking to you.",
    ]
    return random.choice(replies)