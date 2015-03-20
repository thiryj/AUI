#Written by John Thiry - 2015

#some lists contain time sensitive phrases
import AUI_utils
import random

#declare global stock phrases
phrase_list_user_name = ["Honored Human", "Revered One", "Illuminated One", "Nice Human"]
phrase_list_looking_up_answer = ["Checking on that", "One moment while I look that up","Wait a tick","On it"]
phrase_list_greeting = ["Hello", "Hello, ","Hi there","Greetings","Good " + AUI_utils.time_aware_greeting()+ ", "]
phrase_list_affirmative = ["Ok", "Yes", "Got it", "Roger that"]
phrase_list_negative = ["No", "Nope", "Don't think so", "No can do", "Sorry"]
phrase_list_please = ["please", "if you don't mind"]
phrase_list_solicit_command = ["How can I help you?", "What can I do for you?", "What's on your mind?"]
phrase_list_bad_input = ["Would you please repeat that?", "I'm sorry, I didn't hear that", "Please repeat that ",  \
                         "Pardon?"]
phrase_list_waiting_for_input = ["No hurry, I'm here when you need me"]
phrase_list_greet_user = ["Ah!  Now I recognize you, ", "Good to hear you, "]

#declare global recognize key words
keyword_list_quit = ["quit","cancel","stop","good bye"]
keyword_list_user_identify = ["my name is", "this is", "I am"]
keyword_list_home_automation_triggers = ["turn the lights off", "turn the lights on", "turn on","turn up", \
                                         "turn down", "turn off", "lower the", "raise the", "control the", "turn the"]
keyword_list_home_automation_devices = ["foyer", "kitchen", "island", "living room", "mud room", "tv front", \
                                        "tv back", "all", "house"]
keyword_list_home_automation_control_up = ["up", "brighter", "on"]
keyword_list_home_automation_control_down = ["down", "dimmer", "off"]

#declare global constants
AUI_System_Name = "Vanessa"  #Vonase: VOice NAvigated Search Engine
family_names = ['John','Kris','Kristin','Fran','Franny','Frances','Lisi', \
                'Elise','Gabby','Gabrielle','Ellie','Eleanor']
Control4_devices = {'dining room': 212, 'kitchen': 214,'tv back': 216,'tv front': 218,'fire place': 220, \
                    'pendants': 222, 'island pendants': 222, 'counter': 224,'foyer': 230,'mud room': 232, \
                    'island cans': 226,'family room': 231}


