import time
import urllib
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import subprocess
import webbrowser
from utils import *



version = input("Which version are you looking for? (disc/digital): ").strip().lower()

if version == "disc":
    url = 'https://www.target.com/p/playstation-5-console/-/A-81114595'
elif version == "digital":
    url = 'https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596'
else:
    url = 'https://www.target.com/p/forum-novelties-men-s-clown-on-the-town-costume/-/A-80774834?preselect=80787639#lnk=sametab'


browser = open_chrome_driver(url)

refresh_period = ask_refresh_period()
refresh_count = 0
found_stock = False

print("Checking for stock...")
while not found_stock:
    print("Number of tries: ", refresh_count)
    try:
        WebDriverWait(browser, refresh_period).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-test='orderPickupButton']"))).click()
        found_stock = True
    except:
        try:
            WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-test='shipItButton']"))).click()
            found_stock = True
        except:
            refresh_count += 1
            browser.refresh()

print("TARGET IN CART!!")

url = 'https://www.target.com/co-review'

found_stock_redirect(browser, url)
browser.get(url)

for _ in range(5):
    os.system('say "target ps5 in cart"')


