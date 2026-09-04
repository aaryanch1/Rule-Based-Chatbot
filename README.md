# PyBot — Simple Rule-Based Chatbot

A beginner-friendly chatbot built in Python that responds to predefined user
inputs using if-else decision logic. Great for practicing control flow,
basic AI concepts, and clean code structure.

## Features

- **Greeting & exit handling** — recognizes hellos and goodbyes
- **If-else decision logic** — nested conditions route input to the right response
- **Continuous input loop** — chats until the user exits
- **Input sanitization** — trims whitespace and normalizes case before matching
- **Knowledge base** — responses organized by category (greetings, name, jokes, thanks, help) for easy expansion
- **Fallback strategy** — gracefully handles unrecognized input instead of failing
- **Exit strategy** — multiple exit keywords, plus safe handling of Ctrl+C / Ctrl+D

## Requirements

- Python 3.6+
- No external dependencies (uses only the standard library)

## How to Run

```bash
python rule_based_chatbot.py
```

Then just type messages at the `You:` prompt. Type `bye`, `exit`, `quit`,
`goodbye`, `see you`, or `stop` to end the chat.

## Example Session

```
PyBot: Hello! I'm a simple rule-based chatbot. Type 'bye' or 'exit' anytime to leave.

You: hi
PyBot: Hi! Nice to see you.

You: what's your name?
PyBot: I'm PyBot, your friendly rule-based chatbot.

You: tell me a joke
PyBot: Why do programmers prefer dark mode? Because light attracts bugs!

You: asdkjaskjd
PyBot: I'm not sure I understand. Could you rephrase that?

You: bye
PyBot: Goodbye! Have a great day.
```

## Project Structure

```
rule_based_chatbot.py   # Main chatbot script
README.md               # This file
```

## Code Overview

| Function            | Purpose                                                        |
|----------------------|------------------------------------------------------------------|
| `sanitize_input()`  | Cleans and normalizes raw user input                            |
| `get_response()`    | Core if-else logic that matches input against the knowledge base |
| `is_exit_command()` | Checks whether the user wants to quit                           |
| `chat()`             | Runs the main continuous loop                                    |

## Extending the Chatbot

This project is designed to be easy to grow:

1. **Expand the vocabulary** — add more keywords to existing categories in `KNOWLEDGE_BASE`.
2. **Add new categories** — create a new dict entry (e.g., `"weather"`) with its own `keywords` and `responses`, then add a matching `elif` branch in `get_response()`.
3. **Smarter matching** — replace simple substring checks with fuzzy matching (e.g., Python's `difflib.get_close_matches`) to handle typos.
4. **Give it a personality** — rewrite the response strings in a consistent tone/voice (sarcastic, formal, cheerful, etc.).
5. **Treat weird output as feedback** — if the fallback response fires often for a certain phrase, that's a signal to add a new rule for it.

## License

Free to use and modify for learning purposes.
