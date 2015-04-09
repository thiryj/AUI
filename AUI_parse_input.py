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

def which_list_item_is_in_dict_keys(mydict,input_string,prohibited=None):
    wordList = re.sub("[^\w]", " ",  input_string).split()
    print("prohibited list is " + str(prohibited))
    for word in wordList:
        if word not in prohibited:
            for key in mydict.keys():
                print("checking " + word + " for is it in channel key " + key)
                if word.lower() in key.lower():
                    return word        
    
