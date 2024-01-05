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
from players import allplayers
from setlineup import setLineup

driver = webdriver.Safari()
driver.get('https://fantasy.espn.com/basketball/team?leagueId=481644828&teamId=6&seasonId=2024')
email = input("what is your espn login")
password = input("what is your espn login password")
driver.maximize_window()

def login(driver, email, upass):
    ##Open Initial Log In Location
    time.sleep(5)
    driver.switch_to.frame("oneid-iframe")
    print('Switching to iFrame')
    time.sleep(10)
    username = driver.find_element(By.XPATH, "//input[@id='InputIdentityFlowValue']")
    cont = driver.find_element(By.XPATH, "//button[@id='BtnSubmit']")
    username.click()
    username.send_keys(email)
    time.sleep(20)
    cont.click()
    print("button clicked")
    time.sleep(20)
    password = driver.find_element(By.XPATH, "//input[@id='InputPassword']")
    password.click()
    password.send_keys(upass)
    print("sent pass")
    time.sleep(3)
    cont = driver.find_element(By.XPATH, "//button[@id='BtnSubmit']")
    cont.click()
    print("into website")
    time.sleep(10)

login(driver, email, password)
driver.switch_to.default_content()

setLineup(driver, allplayers(driver))

driver.quit()



