import json
from googletrans import Translator

# Install required libraries:
# pip install googletrans==4.0.0-rc1


# Load the input.json file
with open('input.json', 'r') as file:
    data = json.load(file)


# Initialize the translator
translator = Translator()

