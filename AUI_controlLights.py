'''
Author: sapatel91
Date: March 2, 2014
File: lightsControl4.py
Purpose: Set or get Control4 light intensity
Disclaimer: USE AT YOUR RISK, I TAKE NO RESPONSIBILITY
            Most likely there won't be any though
'''
import socket
import time
import AUI_constants
import AUI_parse_input
import AUI_tts
import AUI_sr
from bs4 import BeautifulSoup

#set local constants
C4SOAP_NAME = "\"SendToDeviceAsync\""
ASYNC_STATE = "\"1\""
TCP_IP = '192.168.1.111'
TCP_PORT = 5020
BUFFER_SIZE = 8192
ENCODING = "utf-8"
MESSAGE_TERMINATION = "\0"
PARAM_NAME_DATA = "\"data\""
PARAM_NAME_DATA_TYPE = "\"STRING\""
PARAM_NAME_DEVICE = "\"idDevice\""
PARAM_NAME_DEVICE_TYPE = "\"INT\""
COMMAND_SETLEVEL = "SET_LEVEL"
COMMAND_SETTEMP = "V1 HEAT_SETPOINT"
DO_NOT_PARSE = ["channel","2"]

#set some module variables
timeout = 2
'''
Sets intensity of dimmer switch
Parameters: 
    id - Device ID
    value - 0 to 100
'''
def setLevel(id, value):

    directorConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    directorConn.connect((TCP_IP,TCP_PORT))
    Message_Header_Open = "<c4soap name=" + C4SOAP_NAME + " async=" + ASYNC_STATE + ">"
    Param_1_Open = "<param name=" + PARAM_NAME_DATA + " type=" + PARAM_NAME_DATA_TYPE + ">"
    Command_1_Open = "<devicecommand><command>" + COMMAND_SETLEVEL + "</command>"
    Param_1_2_Set_Open = "<params>"
    Param_1_2_Set_1_Open = "<param><name>LEVEL</name><value type=" + str(PARAM_NAME_DEVICE_TYPE) + "><static>" + str(value) + "</static></value>"
    Param_1_2_Set_1_Close = "</param>"
    Param_1_2_Set_Close = "</params>"
    Command_1_Close = "</devicecommand>"
    Param_1_Close = "</param>"
    Param_2_1_Open = "<param name=" + PARAM_NAME_DEVICE + " type=" + PARAM_NAME_DEVICE_TYPE + ">" + str(id)
    Param_2_1_Close = "</param>"
    Message_Header_Close = "</c4soap>"
    Message = Message_Header_Open + Param_1_Open + Command_1_Open + Param_1_2_Set_Open + Param_1_2_Set_1_Open + Param_1_2_Set_1_Close + \
              Param_1_2_Set_Close + Command_1_Close + Param_1_Close + Param_2_1_Open + Param_2_1_Close + Message_Header_Close
    ##print(Message)
    Messageb = bytes(Message,ENCODING)
    directorConn.sendall(Messageb + bytes(MESSAGE_TERMINATION,ENCODING))
    directorConn.close()

def setHeatTemp(id, value):
    directorConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    directorConn.connect((TCP_IP,TCP_PORT))
    Message_Header_Open = "<c4soap name=" + C4SOAP_NAME + " async=" + ASYNC_STATE + ">"
    Param_1_Open = "<param name=" + PARAM_NAME_DATA + " type=" + PARAM_NAME_DATA_TYPE + ">"
    Command_1_Open = "<devicecommand><command>" + COMMAND_SETLEVEL + "</command>"
    Param_1_2_Set_Open = "<params>"
    Param_1_2_Set_1_Open = "<param><name>LEVEL</name><value type=" + \
                           str(PARAM_NAME_DEVICE_TYPE) + "><static>" + str(value) + "</static></value>"
    Param_1_2_Set_1_Close = "</param>"
    Param_1_2_Set_Close = "</params>"
    Command_1_Close = "</devicecommand>"
    Param_1_Close = "</param>"
    Param_2_1_Open = "<param name=" + PARAM_NAME_DEVICE + \
                     " type=" + PARAM_NAME_DEVICE_TYPE + ">" + str(id)
    Param_2_1_Close = "</param>"
    Message_Header_Close = "</c4soap>"
    Message = Message_Header_Open + Param_1_Open + Command_1_Open + Param_1_2_Set_Open + Param_1_2_Set_1_Open + Param_1_2_Set_1_Close + \
              Param_1_2_Set_Close + Command_1_Close + Param_1_Close + Param_2_1_Open + Param_2_1_Close + Message_Header_Close
    print(Message)
    Messageb = bytes(Message,ENCODING)
    directorConn.sendall(Messageb + bytes(MESSAGE_TERMINATION,ENCODING))
    directorConn.close()


'''
Ramps to a specified level in milliseconds
Parameters:
    id - Device ID
    percent - Intensity
    time - Duration in milliseconds
'''
def rampToLevel(id, percent, time):
    directorConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    directorConn.connect((TCP_IP,TCP_PORT))
    MESSAGE = '<c4soap name="SendToDeviceAsync" async="1"><param name="data" type="STRING"><devicecommand><command>RAMP_TO_LEVEL</command><params><param><name>TIME</name><value type="INTEGER"><static>%d</static></value></param><param><name>LEVEL</name><value type="PERCENT"><static>%d</static></value></param></params></devicecommand></param><param name="idDevice" type="INT">%d</param></c4soap>' % (time, percent, id)
    directorConn.sendall(MESSAGE + "\0")
    directorConn.close()
    
'''
Returns the light level for a dimmer. Value between 0 and 100.
NOTE: will return an error if used on light switches use getLightState instead
'''
def getLevel(id):
    directorConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    directorConn.connect((TCP_IP,TCP_PORT))
    Message = '<c4soap name="GetVariable" async="False"><param name = "iddevice" type = "INT">%d</param><param name = "idvariable" type = "INT">1004</param></c4soap>' % (id)
    Messageb = bytes(Message,ENCODING)
    directorConn.sendall(Messageb + bytes(MESSAGE_TERMINATION,ENCODING))
    #directorConn.sendall(MESSAGE + "\0")
    data = directorConn.recv(BUFFER_SIZE)
    print("data = " + str(data))
    directorConn.close()
    data = BeautifulSoup(data)
    value = data.find("variable")
    value = value.findAll(text=True)
    value = ''.join(value)
    return value

'''
Returns the light state. Output is 0 or 1.
'''
def getLightState(id):
    directorConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    directorConn.connect((TCP_IP,TCP_PORT))
    MESSAGE = '<c4soap name="GetVariable" async="False"><param name = "iddevice" type = "INT">%d</param><param name = "idvariable" type = "INT">1000</param></c4soap>' % (id)
    directorConn.sendall(MESSAGE + "\0")
    data = directorConn.recv(BUFFER_SIZE)
    directorConn.close()
    data = BeautifulSoup(data)
    value = data.find("variable")
    value = value.findAll(text=True)
    value = ''.join(value)
    return value

def cable_channel(channel):
    directorConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    directorConn.connect((TCP_IP,TCP_PORT))
    Message = '<c4soap name="SendToDeviceAsync" async="True"><param type="number" name="iddevice">5</param><param type="string" name="data"><devicecommand><command>' + str(AUI_constants.number_commands.get(int(channel))) + '</command><params></params></devicecommand></param></c4soap>'
    #MESSAGE = '<c4soap name="SendToDeviceAsync" async="1"><param name="data" type="STRING"><devicecommand><command>RAMP_TO_LEVEL</command><params><param><name>TIME</name><value type="INTEGER"><static>%d</static></value></param><param><name>LEVEL</name><value type="PERCENT"><static>%d</static></value></param></params></devicecommand></param><param name="idDevice" type="INT">%d</param></c4soap>' % (time, percent, id)
    #print(Message)
    Messageb = bytes(Message,ENCODING)
    directorConn.sendall(Messageb + bytes(MESSAGE_TERMINATION,ENCODING))
    directorConn.close()

##setLevel(230, 0)
##setHeatTemp(31, 65)
##rampToLevel(264, 50, 3000)
##print getLevel(264)
##print getLightState(276)
##print("getLevel value is "+ getLevel(31))
#if any(phrase in command for phrase in AUI_constants.keyword_list_user_identify):
        #parse command for family names - later use common names lookup
#       AUI_User_Name = AUI_parse_input.which_list_item_is_in_string(AUI_constants.family_names,command)

def cable_channel_master(command):
    mydict = AUI_constants.cable_channels_HD
    #print(mydict.keys())
    desired_channel_name = AUI_parse_input.which_list_item_is_in_dict_keys(mydict,command,DO_NOT_PARSE)
    print("desired channel name is " + str(desired_channel_name))
    if desired_channel_name is not None:
        print("user selected " + str(desired_channel_name))
        
        #establish matching channel dict
        matching_channels = {}
        #get channel number(s)
        for channel_name in mydict.keys():
            if desired_channel_name.lower() in channel_name.lower():
                print("channel name is " + channel_name)
                channel_number = mydict.get(channel_name)
                print("the channel number for " + str(desired_channel_name) + " is " + str(channel_number))
                matching_channels[channel_name]=channel_number
        if len(matching_channels) > 1:
            print("resolve more than one matching channel")
            matching_channel_query = "There is more than one matching channel for " + desired_channel_name + ".  Select the channel number matching the correct channel: \n"
            for matching_channel_name in matching_channels.keys():
                matching_channel_query = matching_channel_query + "[" + str(matching_channels[matching_channel_name]) + "]" + matching_channel_name + "\n"
            #channel_number = input(matching_channel_query)
            channel_number = AUI_sr.mic_input(matching_channel_query, timeout)

        for i in str(channel_number):
            print("setting cable channel to " + i)
            #print("number command is: " + AUI_constants.number_commands.get(int(i)))
            #print("number command is: " + AUI_constants.number_commands.get(2))
            cable_channel(i)
            time.sleep(0.05)
    else:
        #couldn't parse command for channel
        print("can't find the desired channel")



