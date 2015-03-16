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

#declare constants
WAIT_SECONDS = 1

def call_google(mySearchVar):
    #setup
    driver = webdriver.Firefox()
    driver.implicitly_wait(WAIT_SECONDS + 2)
    base_url = "https://www.google.com/"
    gkgText = ""
    gkgAnswer = ""
    gkgDefinition_Word = ""
    gkgDefinition_Detail = ""
    gkgRecipe = ""
    gconvert = ""
    result = ""    
    #run main section
    #print("in selenium section.  Search term is:> " + mySearchVar)
    driver.get(base_url + "")
    if driver.title == "Google":
        driver.find_element_by_id('lst-ib').clear()
        driver.find_element_by_id('lst-ib').send_keys(mySearchVar + Keys.RETURN)
        #driver.find_element_by_id("gbqfb").click()
        content = None
        try:  #google expanded content
            #content = driver.find_element_by_css_selector('div.kno-rdesc')
            content = driver.find_element_by_css_selector("div.kno-rdesc > span").text
            if content is not None:
                gkgText = content
                content = None
        except NoSuchElementException:
            #pass
            print("no expanded wiki answer")
        driver.implicitly_wait(WAIT_SECONDS) #after initial wait, don't wait any longer    
        try:  #google simple answer
            content = driver.find_element_by_css_selector('div._eF').text
            if content is not None:
                gkgAnswer = content
                content = None
        except NoSuchElementException:
            print("no simple answer")
            
##        try:   #google definition word pronunciation
##            content = driver.find_element_by_css_selector('span.lr_dct_ph > span').text
##            if content is not None:
##                gkgDefinition_Word = content
##                print(gkgDefinition_Word)
##                content = None
##        except:
##            #pass
##            print("no definition word")
        
        try:   #google full definition
            content = driver.find_element_by_xpath("//div[@id='uid_0']/div/div/div/div[2]/div[2]/ol/li/div/div/div[2]/div/div/span").text
            if content is not None:
                gkgDefinition_Detail = " the definition of " + mySearchVar + " is " + content
                print(content)
                content = None
        except:
            #pass
            print("no full definition")
        try:
            content = driver.find_element_by_css_selector("/html/body/div[6]/div[3]/div[8]/div[2]/div[3]/div/div[2]/div[2]/div/div[1]/ol/li[1]/div/div/div/div[1]/div/div[1]/div[2]/div/ol/li/div/div/div/div/div/span").text
            if content is not None:
                gkgDefinition_Detail = " the definition of " + mySearchVar + " is " + content
                print(content)
                content = None
        except:
            pass
        
        try:    #google recipe1
            content = driver.find_element_by_css_selector('div._oDd').text
            if content is not None:
                gkgRecipe = content
        except:
            pass
        
        try:    #google recipe2 ._xXc
            content = driver.find_element_by_css_selector('div._xXc').text
            if content is not None:
                gkgRecipe = content
        except:
            pass
                
        try:   #google conversi
            #content = driver.find_element_by_partial_link_text("lhs_div")
            rhs_d = driver.find_element_by_id("ucw_rhs_d").get_attribute("value")
            rhs_u = driver.find_element_by_id("ucw_rhs_u").get_attribute("value")
            if rhs_d != "1":
                if rhs_u == "Foot":
                    content = rhs_d + " Feet "
                else:
                    content = rhs_d + " " + rhs_u + "s"
            else:
                content = rhs_d + " " + rhs_u
            if content is not None:
                gconvert = content
                print("gconvert is: " + str(gconvert))
                content = None
            else:
                print("no conversion")
            try:   #get the question part of the conversion
                lhs_d = driver.find_element_by_id("ucw_lhs_d").get_attribute("value")
                lhs_u = driver.find_element_by_id("ucw_lhs_u").get_attribute("value")
                if lhs_d != "1":
                    if lhs_u == "Foot":
                        convert_query = lhs_d + " Feet " 
                    else:
                        convert_query = lhs_d + " " + lhs_u + "s"
                else:
                    convert_query = lhs_d + " " + lhs_u + " "
                if convert_query is not None:
                    gconvert = convert_query + "is equivalent to " + gconvert
                    #print("gconvert is: " + str(gconvert))
                    content = None
            except:
                pass
                #print("excepted out in try get conversion query")
        except:
            pass
            #print("excepted out in try: by_i. content = " + str(content))
        
        if gkgText or gkgAnswer or gkgDefinition_Word or gkgDefinition_Detail or gkgRecipe != "" or gconvert != "":
            if gkgAnswer != "":
                result = gkgAnswer
            if gkgText != "":
                result = result + ": " + gkgText
            if gkgDefinition_Word != "":
                result = result + gkgDefinition_Word
            if gkgDefinition_Detail != "":
                result = result + gkgDefinition_Detail
            if gkgRecipe != "":
                result = result + gkgRecipe
            if gconvert != "":
                result = gconvert
        else:
            print("could not find result")
            result = "I'm sorry, I am unable to find any information on that topic right now"
    else:
        result = "WRONG_URL"
    #tearDown
    driver.quit()
    return result

  

