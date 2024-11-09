from nltk.chat.util import Chat, reflections
import re
import random

def getcolors(country):
    # Use a context manager to open the file
    # Change the directory and name of the file for personalised use
    with open("flags.txt", "r") as file:
        data = file.read()
        pattern = re.search(rf"{country}:(.*)\n", data)
        if pattern:
            colors = pattern.group(1).strip()
            return colors
        else:
            return "I don't know the colors of that flag."

# Define response pairs with placeholders
pairs = [
    [
        r"hi|hello|good morning|good afternoon",
        ["Hi there, how can I help you!"]
    ],
    [
        r"quit",
        ["GoodBye! Have a nice day."]
    ],
    [
        r"thanks",
        ["You're welcome! Let me know if you have any other questions."]
    ],
    [
        r"what is your name",
        ["I am Nico the flagbot.", "My name is Nico."]
    ],
    [
        r"how many minutes in an hour",
        ["There are 60 minutes in an hour."]
    ],
    [
        r"what are the colors of (.*) flag",
        ["%1: %2"]
    ]
]

# Custom Chat class to handle dynamic response generation
class CustomChat(Chat):
    print("Welcome to flagbot\nType quit to exit")
    def respond(self, statement):
        for pattern, responses in self._pairs:
            match = re.match(pattern, statement)
            if match:
                response = random.choice(responses)  # Select a random response
                if "%1" in response:
                    # Extract the country from the match
                    country = match.group(1)
                    colors = getcolors(country)
                    # Replace placeholders in the response
                    response = response.replace("%1", country).replace("%2", colors)
                return response
        return "I'm sorry, I didn't understand that. Can you Rephrase your question."

# Initialize chatbot with CustomChat class
chatbot = CustomChat(pairs, reflections)
chatbot.converse()
