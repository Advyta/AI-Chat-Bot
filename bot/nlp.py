from textblob import TextBlob

# Expanded keyword-based intent detection
INTENT_KEYWORDS = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "weather": ["weather", "forecast"],
    "time": ["time", "clock"],
    "add_note": ["add note", "write note", "remember this"],
    "show_notes": ["show notes", "list notes", "display notes"],
    "smalltalk": [
        "how are you", "what's up", "what are you doing",
        "tell me about yourself", "who are you"
    ]
}

def detect_intent(text):
    t = text.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(word in t for word in keywords):
            return intent
    return "unknown"

def get_sentiment(text):
    analysis = TextBlob(text).sentiment.polarity
    if analysis > 0.2:
        return "positive"
    elif analysis < -0.2:
        return "negative"
    return "neutral"
