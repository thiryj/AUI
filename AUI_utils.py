#AUI misc uilities
#Written by John Thiry - 2015

import time

def time_aware_greeting():
    mytime = time.localtime().tm_hour
    if 0 <= mytime <= 4:
        return "night"
    elif 5 <= mytime <= 11:
        return "morning"
    elif 12 <= mytime <= 13:
        return "day"
    elif 14 <= mytime <= 17:
        return "afternoon"
    elif 18 <= mytime <= 21:
        return "evening"
    elif 22 <= mytime <= 24:
        return "night"
    else:
        pass
    
    
