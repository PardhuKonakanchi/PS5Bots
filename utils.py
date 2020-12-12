import selenium
from selenium import webdriver
import os
import sys
import subprocess
import webbrowser
import pathlib

def open_chrome_driver(url):
    if sys.platform == 'darwin':    # in case of OS X
        chrome_path = './mac_chromedriver/chromedriver'
    else:
        chrome_path = './windows_chromedriver/chromedriver'

    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(chrome_path, options=options)
    browser.get(url)
    return browser

def ask_refresh_period():
    input("Press Enter once you are logged in...")
    return int(input("Seconds between refresh (would recommend at least 5):"))

def found_stock_redirect(browser, url):
    if sys.platform == 'darwin':    # in case of OS X
        subprocess.Popen(['open', url])
    else:
        webbrowser.open_new_tab(url)
