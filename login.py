# Woring correctyly step 1 completed
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time as t
import json


driver=webdriver.Chrome()

driver.implicitly_wait(15)
driver.get("https://internshala.com/")

driver.find_element(By.XPATH,"//button[@data-target='#login-modal']").click()

driver.find_element(By.XPATH,"//input[@type='email']").send_keys("olympieala2@nerboll.com")

driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Asdf1234@#")

driver.find_element(By.XPATH,"//button[@id='modal_login_submit']").click()

t.sleep(10)

driver.close()