# scikit-learn trains models on your own data. The OpenAI API lets you send any text to a pre-trained language model and get back a generated response.
#  These are two different kinds of intelligence working together.
#  This lesson covers how to structure OpenAI API calls and how to use them in production scripts.

# The OpenAI API requires an active key and makes live network calls.
#  The browser terminals simulate the API structure and response format using hardcoded Python dicts so you can learn 
# the code pattern without spending API credits. The VS Code blocks show the exact production code.

# How the chat API works
# The OpenAI Chat API accepts a list of messages (a conversation history) and returns the model's next message.
#  Each message has a role (system, user, or assistant) and content (the text).
#  The model reads the full conversation history and generates the next assistant turn.

# Think of a briefed analyst.
# You give them a job description (system prompt): "You are an SMP fitness coach. Be direct and practical.
# " Then you give them a task (user message): "James slept 6 hours and hit 7,800 steps today. 
# What should he do differently tomorrow?" They read both, then respond in the voice you specified.
#  The messages list is that briefing plus the ongoing conversation.