#Google search module
#Written by John Thiry - 2015

#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re

import AUI_tts

def get_tempOut(mySearchVar):
    #Audible feedback
    AUI_tts.say("one moment while I check the outside temperature in " + mySearchVar)
    #setup
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    base_url = "https://www.google.com/"
    modSearchVar = "what is the temperature in " + mySearchVar   
    #run main section
    driver.get(base_url + "")
    if driver.title == "Google":
        driver.find_element_by_id('lst-ib').clear()
        driver.find_element_by_id('lst-ib').send_keys(modSearchVar + Keys.RETURN)        #driver.find_element_by_id("gbqfb").click()
        #gkgText = driver.find_element_by_css_selector("div.kno-rdesc > span").text
        tempOut = driver.find_element_by_id("wob_tm").text
        result = "the outside temperature in " + mySearchVar + " is " + tempOut + " degrees Farenheit"
    else:
        result = "WRONG_URL"
    #tearDown
    driver.quit()
    return result
    
