# 🤖 AI Chat Bot

A conversational AI chatbot that understands user intent and sentiment to provide contextual responses.

## Main Features

### 1. **Intent Detection**

- Recognizes different user intents including:
  - **Greeting**: Detects when users say hello
  - **Goodbye**: Recognizes farewell messages
  - **Small Talk**: Handles casual conversations
  - **Time Queries**: Responds to time-related questions
  - **Weather Queries**: Provides weather information
  - **Note Management**: Allows users to add and view notes
  - **Fallback**: Handles unknown requests gracefully

### 2. **Sentiment Analysis**

- Analyzes the emotional tone of user messages
- Adjusts bot responses based on detected sentiment:
  - **Positive**: Enthusiastic and friendly responses
  - **Negative**: Empathetic and supportive responses

### 3. **Emotion-Aware Responses**

- Adapts greetings based on user sentiment
- Provides emotionally intelligent interactions

### 4. **Note Management**

- **Add Notes**: Users can save notes using natural language
- **View Notes**: Retrieve and display all saved notes
- **Persistent Storage**: Notes are stored in `data/notes.json`

### 5. **Command Handlers**

The bot includes specialized handlers for:

- Time information
- Weather updates
- Small talk and casual conversation
- Goodbye messages

## Project Structure

```
ai_bot/
├── main.py              # Main bot entry point
├── bot/
│   ├── nlp.py          # NLP functions (intent detection, sentiment analysis)
│   ├── commands.py     # Command handlers
│   ├── notes.py        # Note management functions
│   └── __pycache__/
├── data/
│   └── notes.json      # Persistent note storage
└── venv/               # Virtual environment
```

## Usage

Run the chatbot:

```bash
python main.py
```

Type `exit` to quit the application.

## Example Interactions

- **User**: "Hello!" → **Bot**: "Hey! Great to see you 😊"
- **User**: "What time is it?" → **Bot**: Displays current time
- **User**: "Add a note: Remember to call Mom" → **Bot**: "Note saved!"
- **User**: "Show my notes" → **Bot**: Displays all saved notes
- **User**: "Goodbye" → **Bot**: Farewell message
