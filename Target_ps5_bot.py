import time
import urllib
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import subprocess
import webbrowser

## STEP 0 ##

# Run 'pip install -r installer.txt' or 'pip3 install -r installer.txt'

## STEP 1 ##

# Download the latest stable chromedriver from this site: 
# https://chromedriver.chromium.org
# input the file path below. usually just a username on mac. Otherwise change appropriately on windows

## STEP 2 ##

# run either python3 Target_ps5_bot.py or python Target_ps5_bot.py

## For target, we will open a browser and let you login before checking stock.
## You can leave it running and it will auto add to cart, and open up checkout page in default browser

version = input("Which version are you looking for? (disc/digital): ").strip().lower()

if version == "disc":
    url = 'https://www.target.com/p/playstation-5-console/-/A-81114595'
elif version == "digital":
    url = 'https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596'
else:
    url = 'https://www.target.com/p/forum-novelties-men-s-clown-on-the-town-costume/-/A-80774834?preselect=80787639#lnk=sametab'

options = webdriver.ChromeOptions()
browser = webdriver.Chrome('./chromedriver', options=options)
browser.get(url);
found_stock = False

input("Press Enter once you are logged in...")
refresh_period = int(input("Seconds between refresh (would recommend at least 5):"))
refresh_count = 0
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
browser.get(url)
if sys.platform == 'darwin':    # in case of OS X
    subprocess.Popen(['open', url])
else:
    webbrowser.open_new_tab(url)

for _ in range(5):
    os.system('say "target ps5 in cart"')


