#Main
#Written by John Thiry - 2015

#import AUI modules
import AUI_tts
import AUI_sr
import AUI_google_search
import AUI_tempOut
import AUI_calc
import AUI_parse_input
import AUI_utils
import AUI_constants

#import recipe module
#import AUI_recipe

#other imports
import random

#initialize local variables
user_quit_command = False
timeout = 2

#announce SR is online
AUI_tts.report_online(AUI_constants.AUI_System_Name)

#set initial query prompt
#query_prompt = "Hello, Gabby.  Would you like to search, check outside temperature, do a unit conversion, get recipe help or do some math?"
query_prompt = random.choice(AUI_constants.phrase_list_greeting) + ". " + random.choice(AUI_constants.phrase_list_solicit_command)

#run main loop
#get user input, fetch answer from internet, return answer, repeat
while user_quit_command is False:
    command = AUI_sr.mic_input(query_prompt, timeout)
    if command == LookupError:
        query_prompt = random.choice(AUI_constants.phrase_list_bad_input)
        continue
        
    if command == TimeoutError:
        #user didn't say command in time - maybe they want more time?
        query_prompt = random.choice(AUI_constants.phrase_list_waiting_for_input)
        timeout = None
        continue
        
    if any(phrase in command for phrase in AUI_constants.keyword_list_user_identify):
        #parse command for family names - later use common names lookup
        AUI_User_Name = AUI_parse_input.which_list_item_is_in_string(AUI_constants.family_names,command)
        AUI_tts.say(random.choice(AUI_constants.phrase_list_greet_user)+ AUI_User_Name)
        query_prompt = random.choice(AUI_constants.phrase_list_solicit_command)
        continue
        
    if "search" in command or "google" in command:
        searc_term = AUI_sr.mic_input("What should I google for you.")
        AUI_tts.say("working on that")
        search_result = AUI_google_search.call_google(search_term)
        AUI_tts.say(search_result)
        continue

    elif "convert" in command or "conversion" in command:
        search_term = AUI_sr.mic_input("What units should I convert?")
        AUI_tts.say("Really?  Do you think I have nothing better to do?  Checking now.")
        search_result = AUI_google_search.call_google(search_term)
        AUI_tts.say(search_result)
        continue
        
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
                temperature_loop = True    
        AUI_tts.say(search_result)
        continue
            
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
        continue
        
    #deprecate recipe function - google handles this now
    #elif "recipe" in command:
    #    recipe_loop = True
    #    while recipe_loop is True:
    #        recipe_loop = False
    #        selected_recipe = AUI_sr.mic_input("Which recipe would you like?")
    #        AUI_tts.say(AUI_recipe.recipe_full_report(selected_recipe))
            
    elif "quit" in command or "cancel" in command or "stop" in command:
        user_quit_command = True
        search_result = ""
        break
    
    elif "pause" in command:
        #implement pausing AUI until wakeup keyword is spoken again
        pass
    
    else: #assume user is doing a google search
        AUI_tts.say("Let me check")
        search_result = AUI_google_search.call_google(command)
        AUI_tts.say(search_result)
       
    #command = AUI_sr.mic_input("Quit or continue?")
##        if command != LookupError:
##            if "quit" in command or "cancel" in command or "stop" in command:
##                user_quit_command = True
##            elif "continue" in command:
##                user_quit_command = False
##                query_prompt = "what else can I do for you?"
##            else:
##                user_quit_command = False
##                #respond to LookupError
##                query_prompt = "anything else?"
##        else:
##            user_quit_command = False
##            #respond to LookupError
##            query_prompt = "Would you please repeat that?"
    
#user elected to quit
AUI_tts.say("Good bye")

        
    
    



