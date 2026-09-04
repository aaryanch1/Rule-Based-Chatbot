"""
Simple Rule-Based Chatbot
--------------------------
Demonstrates control flow, decision-making logic, and basic AI concepts
using if-else statements, an input loop, sanitization, a knowledge base,
a fallback strategy, and a clean exit strategy.
"""

import random

# -----------------------------
# Knowledge base of responses
# -----------------------------
KNOWLEDGE_BASE = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "hola", "yo", "greetings"],
        "responses": [
            "Hello there! How can I help you today?",
            "Hi! Nice to see you.",
            "Hey! What's on your mind?"
        ]
    },
    "how_are_you": {
        "keywords": ["how are you", "how's it going", "how you doing"],
        "responses": [
            "I'm just a bunch of if-else statements, but I'm doing great!",
            "Running smoothly, thanks for asking!"
        ]
    },
    "name": {
        "keywords": ["your name", "who are you", "what are you called"],
        "responses": [
            "I'm PyBot, your friendly rule-based chatbot.",
            "You can call me PyBot!"
        ]
    },
    "help": {
        "keywords": ["help", "what can you do", "commands"],
        "responses": [
            "I can chat about greetings, my name, how I'm doing, tell a joke, "
            "or the time. Type 'bye' or 'exit' to leave."
        ]
    },
    "joke": {
        "keywords": ["joke", "funny", "make me laugh"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I told a UDP joke once... but I don't know if you got it."
        ]
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "appreciate it"],
        "responses": [
            "You're welcome!",
            "Anytime, happy to help!"
        ]
    }
}

# Words/phrases that trigger the chatbot to exit
EXIT_COMMANDS = ["bye", "exit", "quit", "goodbye", "see you", "stop"]

# Fallback responses when nothing matches
FALLBACK_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Hmm, I don't have an answer for that yet. Try asking something else!",
    "Sorry, I didn't quite get that. Type 'help' to see what I can do."
]


def sanitize_input(user_input: str) -> str:
    """Clean and normalize user input for reliable matching."""
    return user_input.strip().lower()


def get_response(user_input: str) -> str:
    """
    Core decision-making logic.
    Checks sanitized input against the knowledge base using if-else logic
    and nested conditions, and falls back gracefully if nothing matches.
    """
    cleaned = sanitize_input(user_input)

    # Guard clause: empty input
    if not cleaned:
        return "You didn't say anything — try typing a message!"

    # Nested condition example: check each category's keywords
    if any(word in cleaned for word in KNOWLEDGE_BASE["greeting"]["keywords"]):
        return random.choice(KNOWLEDGE_BASE["greeting"]["responses"])

    elif any(phrase in cleaned for phrase in KNOWLEDGE_BASE["how_are_you"]["keywords"]):
        return random.choice(KNOWLEDGE_BASE["how_are_you"]["responses"])

    elif any(phrase in cleaned for phrase in KNOWLEDGE_BASE["name"]["keywords"]):
        return random.choice(KNOWLEDGE_BASE["name"]["responses"])

    elif any(phrase in cleaned for phrase in KNOWLEDGE_BASE["help"]["keywords"]):
        return random.choice(KNOWLEDGE_BASE["help"]["responses"])

    elif any(word in cleaned for word in KNOWLEDGE_BASE["joke"]["keywords"]):
        return random.choice(KNOWLEDGE_BASE["joke"]["responses"])

    elif any(word in cleaned for word in KNOWLEDGE_BASE["thanks"]["keywords"]):
        return random.choice(KNOWLEDGE_BASE["thanks"]["responses"])

    else:
        # Fallback strategy: no rule matched
        return random.choice(FALLBACK_RESPONSES)


def is_exit_command(user_input: str) -> bool:
    """Check if the sanitized input matches an exit command."""
    cleaned = sanitize_input(user_input)
    return any(cmd in cleaned for cmd in EXIT_COMMANDS)


def chat():
    """Main continuous input loop running the chatbot."""
    print("PyBot: Hello! I'm a simple rule-based chatbot. "
          "Type 'bye' or 'exit' anytime to leave.\n")

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            # Graceful exit strategy for Ctrl+C / Ctrl+D
            print("\nPyBot: Goodbye! Take care.")
            break

        if is_exit_command(user_input):
            print("PyBot: Goodbye! Have a great day.")
            break

        response = get_response(user_input)
        print(f"PyBot: {response}")


if __name__ == "__main__":
    chat()
