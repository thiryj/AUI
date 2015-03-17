#AUI tts engine
#Written by John Thiry - 2015
import sys
sys.path.append('c:\python34\lib\site-packages\pyttsx')
import pyttsx
engine = pyttsx.init('sapi5')

def report_online(name=None):
    greeting = "I am online and listening.  "
    if name != None:
        greeting = greeting + "Please call me " + name
    engine.say(greeting)
    engine.runAndWait()

def say(text):
    engine.say(text)
    engine.runAndWait()
    
