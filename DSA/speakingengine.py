#text to speech with using pyttsx3 module ..............................
'''
'''
import pyttsx3
# Initialize the text-to-speech engine
engine = pyttsx3.init()
# Set properties (optional)
# Adjust speech rate (words per minute)
engine.setProperty('rate', 140)
# Adjust volume (0.0 to 1.0)
engine.setProperty('volume', 10)
# Text to be spoken
text = "Hello, world! This is a text-to-speech example using pyttsx3 on Windows , hello! rahul sir good morning ! how can i help you "

# Speak the text
engine.say(text)

# Run the engine and wait for the speech to complete
engine.runAndWait()

# Stop the engine (important for clean shutdown)
engine.stop()
'''

# if we run code in vs code it only speak first sentence 
'''
import pyttsx3
import json
engine =pyttsx3.init()

engine.setProperty('rate',100)
engine.setProperty('volume',10)
with open('r.json' ,'r') as f:
    text =json.load(f)
str(text)
names ='i found a girl beautiful and sweet mere haaht m tera haath ho saari jannte mere saat ho '
engine.say(names)
engine.say(text)
engine.runAndWait()
engine.stop()
'''
'''
# speech to text by using google free api  key .......................................
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('speak something .....')
    audio =r.listen(source)

text = r.recognize_google(audio)

print(text)
