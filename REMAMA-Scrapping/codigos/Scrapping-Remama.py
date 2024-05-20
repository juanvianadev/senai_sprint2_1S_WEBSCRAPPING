import time
import driver
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://www.instagram.com/"

driver.get(url)
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("web_scrap_ciencia")
driver.find_element(By.NAME, "password").send_keys("0000@@")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
time.sleep(3)

url2 = "https://www.instagram.com/remamadragaorosa/"
driver.get(url2)
time.sleep(2)

Posts = []
Posts = driver.find_elements(By.CLASS_NAME, "_aagw")[0:25]

Posts1 = Posts[7].click()
time.sleep(3)
driver.back()
time.sleep(3)

curtidas = []

#for post in Posts:
 #    post.click()
 #    time.sleep(2)
   #  curtida = driver.find_element(By.CLASS_NAME, "x1lliihq").find_element(By.CLASS_NAME, "html-span").text
   #  curtidas = curtidas.append(curtida)
   #  driver.back()
    # time.sleep(2)

#print(curtidas)