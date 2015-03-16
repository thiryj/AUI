#Main
#Written by John Thiry - 2015

#import text to speech 
import AUI_tts

#$#4#import speech recog
import AUI_sr

#import google search module
import AUI_google_search

#import google outside temperature module
import AUI_tempOut

#import google math module
import AUI_calc

#import recipe module
import AUI_recipe

#initialize variables
user_quit_command = False

#declare constants

search_term = "how do you make hot cocoa"

search_result = AUI_google_search.call_google(search_term)
print(search_result)
    



