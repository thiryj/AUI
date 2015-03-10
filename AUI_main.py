#Main
#Written by John Thiry - 2015

#import text to speech 
import AUI_tts

#import speech recog
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

#announce SR is online
AUI_tts.report_online()

#determine command type
#query_prompt = "Hello, Gabby.  Would you like to search, check outside temperature, do a unit conversion, get recipe help or do some math?"
query_prompt ="how can I help you?"
while user_quit_command is False:
    command = AUI_sr.mic_input(query_prompt)
    if "search" in command or "google" in command:
        search_term = AUI_sr.mic_input("What should I google for you.")
        AUI_tts.say("working on that")
        search_result = AUI_google_search.call_google(search_term)
        AUI_tts.say(search_result)

    elif "convert" in command or "conversion" in command:
        search_term = AUI_sr.mic_input("What units should I convert?")
        AUI_tts.say("Really?  Do you think I have nothing better to do?  Checking now.")
        search_result = AUI_google_search.call_google(search_term)
        AUI_tts.say(search_result)
        
    elif "temperature" in command:
        tempterature_loop = True
        while tempterature_loop is True:
            if "outside" in command:
                tempterature_loop = False
                location = AUI_sr.mic_input("For what city and state would you like the temperature?")
                search_result = AUI_tempOut.get_tempOut(location)
            elif "inside" in command:
                tempterature_loop = True #change this to False when inside temp is implemented
                AUI_tts.say("I'm sorry, I can't check inside temperature yet")
                command = AUI_sr.mic_input("Did you want the outside or inside temperature or quit?")
                if "quit" in command or "cancel" in command or "stop" in command:
                    tempterature_loop = False
                    search_result = ""
            else:
                command = AUI_sr.mic_input("Did you want the outside or inside temperature?")
            AUI_tts.say(search_result)
            
    elif "math" in command:
        math_loop = True
        while math_loop is True:
            math_problem = AUI_sr.mic_input("Please state your math problem?")
            if math_problem != LookupError:
                math_loop = False
                search_result = AUI_calc.solve(math_problem)
                if search_result == "UNDEFINED_MATH_PROBLEM":
                    AUI_tts.say("I couldn't understand the question")
                    math_loop = True
        AUI_tts.say(search_result)
        
    elif "recipe" in command:
        recipe_loop = True
        while recipe_loop is True:
            recipe_loop = False
            selected_recipe = AUI_sr.mic_input("Which recipe would you like?")
            AUI_tts.say(AUI_recipe.recipe_full_report(selected_recipe))
            
    elif "quit" in command or "cancel" in command or "stop" in command:
        user_quit_command = True
        search_result = ""
    else: #assume user is doing a google search
        search_result = AUI_google_search.call_google(command)
        AUI_tts.say(search_result)
    #else:  
     #   AUI_tts.say("I'm afraid I don't know how to do that yet")
        
    command = AUI_sr.mic_input("Quit or continue?")
    if "quit" in command:
        user_quit_command = True
    else:
        query_prompt = "I'm sorry, I didn't get that"
        user_quit_command = False
AUI_tts.say("Good bye")

        
    
    



