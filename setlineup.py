import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

def setLineup(driver, players):
    numplaying = playersplaying(players)
    numnp = 13 - numplaying
    benchedplayers = players[10:]
    for i in range(10):
        if players[i][0] != "Bench":
            if players[i][3] != "NP":
                if numplaying > 10:
                    for j in range(3):
                        if benchedplayers[j][3] != "NP" and cantakespot(players[i], benchedplayers[j]) and shouldtakespot(players[i], benchedplayers[j]):
                           moveplayer(driver, players[i], benchedplayers[j], players[i][-1], benchedplayers[j][-1])
                           break
                        else:
                            pass
            else:
                for j in range(3):
                    if benchedplayers[j][3] != "NP" and cantakespot(players[i], benchedplayers[j]):
                        moveplayer(driver, players[i], benchedplayers[j], players[i][-1], benchedplayers[j][-1])
                        break
                    else:
                        pass
        else:
            pass


def cantakespot(player1, player2):
    allpos = player2[2].split(", ")
    #utlities
    if player1[0] == 'UTIL':
        return True
    #starter
    elif player1[0] in allpos:
        return True
    #G or F
    elif player1[0] == 'G':
        if 'SG' in allpos or 'PG' in allpos:
            return True
        else:
            return False
    elif player1[0] == 'F':
        if 'SF' in allpos or 'PF' in allpos:
            return True
        else:
            return False
    else:
        return False
    
def shouldtakespot(player1, player2):
    if player1[-2] >= player2[-2]:
        return True
    else:
        return False
    
def moveplayer(driver, player1, player2, tr1, tr2):
    try:
        driver.find_element(By.XPATH, "//*[@id='fitt-analytics']/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[" + tr1 + "]/td[3]/div/div/button").click()
    except:
        driver.switch_to.default_content()
    herebutton = "//*[@id='fitt-analytics']/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[" + tr2 + "]/td[3]/div/div/button"
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, herebutton)))
        element.click()
    except: 
        driver.find_element(By.XPATH, "//*[@id='fitt-analytics']/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[" + tr1 + "]/td[3]/div/div/button").click()

def playersplaying(players):
    count = 0
    for i in range(len(players)):
        if players[i][3] != "NP":
            count += 1
        else:
            pass
    return count
