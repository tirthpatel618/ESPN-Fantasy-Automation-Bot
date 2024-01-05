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


def allplayers(driver):
    player = []
    playerlist = []
    for i in range(13):
        player.append(driver.find_element(By.XPATH, "//*[@id='fitt-analytics']/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[" + str(i + 1)  + "]/td[1]/div").text)
        player.append(driver.find_element(By.XPATH, "//*[@id='fitt-analytics']/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[" + str(i + 1) + "]/td[2]/div/div/div[2]/div/div[1]/span/a").text)
        player.append(driver.find_element(By.XPATH, "//*[@id='fitt-analytics']/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[" + str(i+1) + "]/td[2]/div/div/div[2]/div/div[2]/span[2]").text)
        try:
            player.append(driver.find_element(By.XPATH, "//*[@id='fitt-analytics']/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[" + str(i + 1) +  "]/td[5]/div/div/span/a").text)
        except:
            player.append("NP")
        
        try:
            player.append(driver.find_element(By.XPATH, "//*[@id='fitt-analytics']/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[" + str(i+1) + "]/td[2]/div/div/div[2]/div/div[1]/span[2]").text)
        except:
            player.append("Healthy")
        player.append(driver.find_element(By.XPATH, "//*[@id='fitt-analytics']/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/div/div[2]/table/tbody/tr[" + str(i+1) + "]/td[13]/div").text)
        player.append(str(i+1))
        playerlist.append(player)
        player = []

    return playerlist


