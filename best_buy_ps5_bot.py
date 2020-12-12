import time
import urllib
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import sys
import subprocess

import os

## STEP 0 ##

# Run 'pip install -r installer.txt' or 'pip3 install -r installer.txt'

## STEP 1 ##

# Download the latest stable chromedriver from this site: 
# https://chromedriver.chromium.org
# input the file path below. usually just a username on mac. Otherwise change appropriately on windows

## STEP 2 ##

# run either 'python3 best_buy_ps5_bot.py' or 'python best_by_ps5_bot.py'

version = input("Which version are you looking for? (disc/digital/3080) or enter your own url: ").strip().lower()

if version == "disk":
    url = 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'
elif version == "digital":
    url = 'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161'
elif version == "3080":
    url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
else:
    url = version


options = webdriver.ChromeOptions()
browser = webdriver.Chrome('./chromedriver', options=options)
browser.get(url)
found_stock = False

input("Press enter when logged in...")
print("Checking for stock...")
refresh_period = int(input("Seconds between refresh (would recommend at least 5 for your computer's sake):"))
refresh_count = 0
while not found_stock:
    print("Number of tries: ", refresh_count)
    try:
        add_to_cart = browser.find_element_by_css_selector("button[class*='add-to-cart-button']").click()
        if add_to_cart.isEnabled():
            add_to_cart.click()
            found_stock = True
    except:
        time.sleep(refresh_period)
        refresh_count += 1
        browser.refresh()


print("BEST BUY IN STOCK!!")

if sys.platform == 'darwin':    # in case of OS X
    subprocess.Popen(['open', url])
else:
    webbrowser.open_new_tab(url)

for _ in range(5):
    os.system('say "best buy ps5 in stock"')

add_to_cart_ready = False

browser.implicitly_wait(1)
print("Waiting to get past queue and add to cart...")
while not add_to_cart_ready:
    try:
        add_to_cart = browser.find_element_by_css_selector("button[class*='add-to-cart-button']").click()
        if add_to_cart.isEnabled():
            add_to_cart.click()
            found_stock = True
    except:
        time.sleep(1)

print("BEST BUY IN CART!!")

for _ in range(5):
    os.system('say "best buy ps5 in cart"')