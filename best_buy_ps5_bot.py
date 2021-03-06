import time
import urllib
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import sys
import subprocess
from utils import *

import os

version = input("Which version are you looking for? (disc/digital/3080) or enter your own url: ").strip().lower()

if version == "disc":
    url = 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'
elif version == "digital":
    url = 'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161'
elif version == "3080":
    url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
else:
    url = version


browser = open_chrome_driver(url)

input("Press enter to continue once logged in...")

hear_alarm = input("Do you want to hear alarm when in stock and in cart? (Y/N): ").strip().lower()

want_refresh = input("Do you want the browser to refresh (check github page for explanation) Y/N: ").strip().lower()

if want_refresh == "y":
    refresh_period = ask_refresh_period()
else:
    refresh_period = 1

found_stock = False

print("Checking for stock...")

refresh_count = 0
browser.implicitly_wait(refresh_period)
while not found_stock:
    print("Number of tries: ", refresh_count)
    try:
        add_to_cart = browser.find_element_by_css_selector("button[class*='add-to-cart-button']")
    except:
        refresh_count += 1
        if want_refresh == "y":
            browser.refresh()
    if add_to_cart.is_enabled():
        print("Found it!")
        add_to_cart.click()
        found_stock = True
    else:
        time.sleep(refresh_period)
        refresh_count += 1
        if want_refresh == "y":
            browser.refresh()


print("BEST BUY IN STOCK!!")

found_stock_redirect(browser, url)

if hear_alarm == "y":
    for _ in range(5):
        os.system('say "best buy in stock"')

add_to_cart_ready = False

browser.implicitly_wait(1)
print("Waiting to get past queue and add to cart...")
while not add_to_cart_ready:
    add_to_cart = browser.find_element_by_css_selector("button[class*='add-to-cart-button']")
    if add_to_cart.is_enabled():
        add_to_cart.click()
        add_to_cart_ready = True
    else:
        time.sleep(1)

print("BEST BUY IN CART!!")

found_stock_redirect('https://www.bestbuy.com/cart')
browser.get(url)

if hear_alarm == "y":
    for _ in range(5):
        os.system('say "best buy in cart"')