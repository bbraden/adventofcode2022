from __future__ import print_function
from calendar import c
import re
import os
import sys
import time
import random
from time import sleep
from itertools import groupby
from selenium import webdriver
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException

if __name__ == "__main__":
    load_dotenv()

    gmail_username = os.getenv("gmail_username")
    gmail_password = os.getenv("gmail_password")
    
    print("Username: " +gmail_username)
    print("Password: " +gmail_password)

    driver = uc.Chrome()
    print("drive")
    driver.get("https://membean.com/login")
    sleep(5)

    driver.find_element("xpath", '//*[@id="content"]/section/ul/li[1]/a').click()
    sleep(5)

    #input username
    username = driver.find_element("xpath", '//*[@id="identifierId"]')
    username.send_keys(gmail_username)
    driver.find_element("xpath", '//*[@id="identifierNext"]/div/button/span').click()
    sleep(5)

    #input password
    password = driver.find_element("xpath", '//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys(gmail_password)
    driver.find_element("xpath", '//*[@id="passwordNext"]/div/button/span').click()
    sleep(20)

    #Start Training Select 15 minutes and Proceed
    driver.get("https://membean.com/training_sessions/new")
    sleep(20)

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element("xpath", xpath)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_css(css):
        try:
            driver.find_element(By.CSS_SELECTOR, css)
        except NoSuchElementException:
            return False
        return True

    if check_exists_by_xpath('//*[@id="15_min_"]') == True:
        driver.find_element("xpath", '//*[@id="15_min_"]').click()
        sleep(4)
        
    i = 1
    while i < 100:
        try:
            #if Question type: Single is found
            if check_exists_by_css('#single-question > h3') == True:
                print("Question type: Single")
                passEvent = driver.find_element("xpath", '//*[@id="pass__event"]')
                driver.execute_script("arguments[0].click();", passEvent)
                print("Answered")
                print('\n')
                sleep(4)
            elif check_exists_by_css('#single-question > h3') == False:
                pass

            if check_exists_by_css('#single-question > p') == True:
                print("Question type: Single")
                passEvent = driver.find_element("xpath", '//*[@id="pass__event"]')
                driver.execute_script("arguments[0].click();", passEvent)
                print("Answered")
                print('\n')
                sleep(4)
            elif check_exists_by_css('#single-question > p') == False:
                pass

            #if Question type: Word Fill is found
            if check_exists_by_css('#word-hint') == True:
                print("Question type: Word Fill")
                passEvent = driver.find_element("xpath", '//*[@id="pass__event"]')
                driver.execute_script("arguments[0].click();", passEvent)
                print("Answered")
                print('\n')
                sleep(4)
            elif check_exists_by_css('#word-hint') == False:
                pass

            #if definition page is found
            if check_exists_by_css('#add-note') == True:
                print("Word")
                wordformCon = driver.find_element("id", 'wordform-container')
                wordform = driver.find_element(By.CSS_SELECTOR, '#wordform-container > h1').text
                print(wordform)
                print('\n')
                with open('word.txt', 'w', encoding="utf-8") as n:
                    n.write(f'{wordform}')
                sleep(2)

                if check_exists_by_css('#choice-section > li.choice.answer') == True:
                    print("Question type: Wordpage Question")
                    driver.find_element(By.CSS_SELECTOR, '#choice-section > li.choice.answer').click()
                    print("Answered")
                    print('\n')
                    sleep(4)
                elif check_exists_by_css('#choice-section > li.choice.answer') == False:
                    pass
                
                if check_exists_by_xpath('//*[@id="next-btn"]') == True:
                    driver.find_element("xpath", '//*[@id="next-btn"]').click()
                    sleep(4)
                elif check_exists_by_xpath('//*[@id="next-btn"]') == False:
                    pass
            elif check_exists_by_css('#add-note') == False:
                pass
            
            #if spelling page is found
            if check_exists_by_xpath('//*[@id="wordspell-wrapper"]') == True:
                sleep(4)
                print("Wordspell")
                passEvent = driver.find_element("xpath", '//*[@id="pass__event"]')
                driver.execute_script("arguments[0].click();", passEvent)
                print("Answered")
                print('\n')
            elif check_exists_by_xpath('//*[@id="wordspell-wrapper"]') == False:
                pass
            
            #if ornament is found
            if check_exists_by_xpath('//*[@id="interstitial"]/img') == True:
                print("Ornament")
                print('\n')
                sleep(4)

                #event for when the close session button comes on
                if check_exists_by_xpath('//*[@id="Click_me_to_stop"]') == True:
                    driver.find_element("xpath", '//*[@id="Click_me_to_stop"]').click()
                    print("Session Ended")
                    print('\n')
                    if os.path.exists("word.txt"):
                        os.remove("word.txt")
                    else:
                        pass
                    break
                elif check_exists_by_xpath('//*[@id="Click_me_to_stop"]') == False:
                    pass

                #event for when anything else comes on
                if check_exists_by_xpath('//*[@id="Let_rsquo_s_continue"]') == True:
                    driver.find_element("xpath", '//*[@id="Let_rsquo_s_continue"]').click()
                elif check_exists_by_xpath('//*[@id="Let_rsquo_s_continue"]') == False:
                    pass
                sleep(2)
           
                #event when a level is passed
                if check_exists_by_xpath('//*[@id="Onward"]') == True:
                    driver.find_element("xpath", '//*[@id="Onward"]').click()
                    print("Level Passed")
                    print('\n')
                    sleep(3)
                elif check_exists_by_xpath('//*[@id="Onward"]') == False:
                    pass
                sleep(2)
                
            elif check_exists_by_xpath('//*[@id="interstitial"]/img') == False:
                pass


        except Exception as e: 
            print(e)
            if os.path.exists("word.txt"):
                os.remove("word.txt")