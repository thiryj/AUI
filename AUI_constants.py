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
                    'island cans': 226,'family room': 231,'Mudroom':232, 'Visor Control':233, 'MyHome - PC':234, 'cable box':261, 'Google TV':277}
number_commands = {0:'NUMBER_0',1:'NUMBER_1',2:'NUMBER_2',3:'NUMBER_3',4:'NUMBER_4',5:'NUMBER_5',6:'NUMBER_6',7:'NUMBER_7',8:'NUMBER_8',9:'NUMBER_9',}
cable_channels_HD = {'Travel Channel HD':182,'HBO HD':300,'Cinemax HD':319,'Showtime HD':339,'The Movie Channel HD':351,'Starz HD':369,'Starz Edge HD':377,'Starz Kids & Family HD':378,'Starz Comedy HD':379,'WHP HD (CBS)':802,'WITF HD (PBS)':803,'WPMT HD (FOX)':804,'WLYH HD (CW)':805,'WHTM HD (ABC)':807,'WGAL HD (NBC)':808,'WGCB HD (IND)':809,'QVC HD':811,'HSN HD':812,'Bloomberg TV HD':814,'The Weather Channel HD':815,'HLN HD':816,'CNN HD':817,'MSNBC HD':818,'CNBC HD':819,'FOX News HD':820,'FOX Business HD':821,'Universal HD':822,'USA Network HD':823,'FX HD':824,'TNT HD':825,'TBS HD':826,'SPIKE TV HD':827,'Comedy Central HD':828,'Syfy HD':829,'Hallmark Channel HD':830,'A&E HD':831,'Bravo HD':832,'E! HD':833,'Esquire Network HD':834,'Lifetime HD':835,'WE tv HD':836,'TLC HD':837,'HGTV HD':838,'Food Network HD':839,'Travel Channel HD':840,'truTV HD':841,'SEC Network HD':842,'ROOT Sports Pittsburgh HD':843,'MASN HD':844,'MASN2 HD':845,'Comcast SportsNet HD':847,'NBC Sports HD':848,'Golf Channel HD':849,'ESPN HD':850,'ESPN2 HD':851,'ESPNews HD':852,'ESPNU HD':853,'CBS Sports Network HD':854,'Big Ten Network HD':855,'The Comcast Network HD':856,'FOX Sports 1 HD':857,'NHL Network HD':858,'MLB Network HD':859,'NFL Network HD':860,'NBA TV HD':863,'TV One HD':865,'BET HD':866,'Animal Planet HD':868,'Discovery Channel HD':869,'Velocity HD':870,'National Geographic HD':871,'Science HD':872,'Destination America HD':873,'FYI HD':874,'HISTORY HD':875,'H2 HD':876,'Disney XD HD':877,'Cartoon Network HD':878,'Nickelodeon HD':879,'Disney Channel HD':880,'ABC Family HD':881,'Palladia HD':882,'CMT HD':883,'MTV HD':884,'Fuse HD':885,'VH1 HD':886,'UPtv HD':887,'AMC HD':889,'TCM HD':890,'ENCORE HD':891,'MGM Television HD':892,'IFC HD':893,'HMM HD':894,'LMN HD':895,'AXS TV HD':897,'Investigation Discovery HD':899,'Smithsonian Channel HD':915,'Sportsman Channel HD':917,'GSN HD':924,'Ovation HD':946,'BBC America HD':1225,'Nat Geo Wild HD':1262,'Oxygen HD':1334,'Sprout HD':1505,'Discovery Family Channel HD':1511,'FXX HD':1715}



