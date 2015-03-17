#Written by John Thiry - 2015

import re

def parse_input(input_string):
    wordList = re.sub("[^\w]", " ",  input_string).split()
    return wordList

def which_list_item_is_in_string(mylist,input_string):
    wordList = re.sub("[^\w]", " ",  input_string).split()
    for list_item in mylist:
        if list_item in wordList:
            return list_item

        
    
