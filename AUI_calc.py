#Google math module
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

def solve(mySearchVar):

    #Audible feedback
    AUI_tts.say("one moment while I work out that answer")

    #setup
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    base_url = "https://www.google.com/"
            
    #run main section
    driver.get(base_url + "")
    if driver.title == "Google":
        driver.find_element_by_id('lst-ib').clear()
        driver.find_element_by_id('lst-ib').send_keys(mySearchVar + Keys.RETURN)
        if driver.find_element_by_id("cwos"):
            answer = driver.find_element_by_id("cwos").text
            result = "the answer to " + mySearchVar + " is " + answer
        else:
            result = "UNDEFINED_MATH_PROBLEM"
    else:
        result = "WRONG_URL"
    #tearDown
    driver.quit()
    return result
