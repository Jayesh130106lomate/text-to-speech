def TextToSpeech(Text, func=lambda r=None: True):
#     Data = str(Text).split(".")  # Split the text by periods into a list of sentences

#     # List of predefined responses for cases where the text is too long
#     responses = [
#         "The rest of the result has been printed to the chat screen, kindly check it out sir.",
#         "The rest of the text is now on the chat screen, sir, please check it.",
#         "You can see the rest of the text on the chat screen, sir.",
#         "The remaining part of the text is now on the chat screen, sir.",
#         "Sir, you'll find more text on the chat screen for you to see.",
#         "The rest of the answer is now on the chat screen, sir.",
#         "Sir, please look at the chat screen, the rest of the answer is there.",
#         "You'll find the complete answer on the chat screen, sir.",
#         "The next part of the text is on the chat screen, sir.",
#         "Sir, please check the chat screen for more information.",
#         "There's more text on the chat screen for you, sir.",
#         "Sir, take a look at the chat screen for additional text.",
#         "You'll find more to read on the chat screen, sir.",
#         "Sir, check the chat screen for the rest of the text.",
#         "The chat screen has the rest of the text, sir.",
#         "There's more to see on the chat screen, sir, please look.",
#         "Sir, the chat screen holds the continuation of the text.",
#         "You'll find the complete answer on the chat screen, kindly check it out sir.",
#         "Please review the chat screen for the rest of the text, sir.",
#         "Sir, look at the chat screen for the complete answer."
#     ]

#     # If the text is very long (more than 4 sentences and 250 characters), add a response message
#     if len(Data) > 4 and len(Text) > 250:
#         TTS(" ".join(Text.split(".")[0:2]) + ". " + random.choice(responses), func)
#     else:
#         # Otherwise, just play the whole text
#         TTS(Text, func)