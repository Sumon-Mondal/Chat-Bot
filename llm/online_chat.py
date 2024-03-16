# Import the Client class from the g4f package
from g4f.client import Client
# Create a client instance
client = Client()

# Send a message to the chatbot
response = client.chat.completions.create(
   # Set the model to gpt-3.5-turbo
   model="gpt-3.5-turbo",
   # Pass a list of message dictionaries as an argument
   messages=[{"role": "user", "content": "Hello"}],
)
def Chat():
# Continue the conversation with the chatbot
    while True:
        # Print the chatbot's response
        
        # Get the user's next message
        user_input = input("You: ")
        
        # Send the user's message to the chatbot
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
        )
        return("Chatbot: " + response.choices[0].message.content)