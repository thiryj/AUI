#Speech Recognition module
#Written by John Thiry - 2015

import time

#import sr engine
import pyaudio

#import AUI tts engine
import AUI_tts

#import sr engine
import speech_recognition as sr

#other constants
myenergy_threshold = 550
show_energy = False      #debugging tool

#listen
def mic_input(prompt, timeout = None):
    r = sr.Recognizer()   
    r.energy_threshold = int(myenergy_threshold)
    #print(r.pause_threshold)
    AUI_tts.say(prompt)
    with sr.Microphone() as source:
        try:
            audio = r.listen(source,timeout)
            if show_energy is True:
                print("energy is " + str(r.energyx))
        except TimeoutError:
            #AUI_tts.say("Sorry, didn't get that")
            return TimeoutError
    try:
        user_audio_input = r.recognize(audio)
        print("Transcription: " + user_audio_input) # recognize speech using Google Speech Recognition
        #AUI_tts.say(sr_feedback)
        return user_audio_input
    except LookupError: # speech is unintelligible
        print("Could not understand audio")
        AUI_tts.say("Could not understand audio")
        return LookupError
        
