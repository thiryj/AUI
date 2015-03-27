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
from bs4 import BeautifulSoup

#set local constants
C4SOAP_NAME = "SendToDeviceAsync"
ASYNC_STATE = "1"
TCP_IP = '192.168.1.111'
TCP_PORT = 5020
BUFFER_SIZE = 8192
ENCODING = "utf-8"
MESSAGE_TERMINATION = "\0"
PARAM_NAME_DATA = "data"
PARAM_NAME_DATA_TYPE = "STRING"
PARAM_NAME_DEVIVE = "idDevice"
PARAM_NAME_DEVIVE_TYPE = "INT"
COMMAND_SETLEVEL = "SET LEVEL"

'''
Sets intensity of dimmer switch
Parameters: 
    id - Device ID
    value - 0 to 100
'''
def setLevel(id, value):

    directorConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    directorConn.connect((TCP_IP,TCP_PORT))
    MESSAGE = '<c4soap name="SendToDeviceAsync" async="1"><param name="data" type="STRING"><devicecommand><command>SET_LEVEL</command><params><param><name>LEVEL</name><value type="INT"><static>%d</static></value></param></params></devicecommand></param><param name="idDevice" type="INT">%d</param></c4soap>' % (value, id)
    MESSAGEb = bytes(MESSAGE,ENCODING)
    directorConn.sendall(MESSAGEb + bytes(MESSAGE_TERMINATION,ENCODING))
    directorConn.close()
    print(MESSAGE)

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
    MESSAGE = '<c4soap name="GetVariable" async="False"><param name = "iddevice" type = "INT">%d</param><param name = "idvariable" type = "INT">1001</param></c4soap>' % (id)
    directorConn.sendall(MESSAGE + "\0")
    data = directorConn.recv(BUFFER_SIZE)
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



##setLevel(230, 0)
setLevel(230, 0)
##rampToLevel(264, 50, 3000)
##print getLevel(264)
##print getLightState(276)

