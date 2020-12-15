# PS5Bots

Note that this solution uses an open WebBrowser which is slightly slower than a JS solution and likely takes up more RAM (but this is all I know how to do lol). The advantage though is that it can do the work of adding to cart and possibly let you checkout quicker without any fishy IP blocking

## Instructions

1. Download repo using green button in top right as zip
2. Make sure your chrome updated to the latest version (V 87.X.X.X)
2. Open up command prompt/terminal and navigate to downloaded folder
3. On Command prompt:

* Run `pip install -r installer.txt` or `pip3 install -r installer.txt` If those don't work, you may need to follow the instructions right below to download python
* run either `python3 best_buy_ps5_bot.py` or `python best_buy_ps5_bot.py` (or whatever file you want to run)
* If pip or python doesn't work, you may need to install python here: https://www.python.org/downloads/. If you already have python, uninstall and redownload **NOTE** : Make sure as you're downloading to check the box that says "Add Python X.X to PATH"

You will be prompted for either disc or digital (and for best buy the 3080 as well). You will also need to login each time you run the script as each instance is like an incognito tab

### Target:

* You will be prompted for either disc or digital
* Once the browser is open, login to your target account
* Press enter to continue
* Enter a refresh period (I recommend at least 5 seconds since this browser does take up computer memory to run)
* Once an in-stock button is available, the bot will add to cart automatically and open your browser to the checkout page (make sure you're logged in there)
* It will also make a sound like it or not since these drops are early and you need to wake up :P

### Best Buy:
 You will be prompted for either disc or digital or 3080 (founders edition) or paste in whatever url you want
* Once the browser is open, login to your best buy account
* Press enter to continue
* Enter a refresh period (I recommend at least 5 seconds since this browser does take up computer memory to run)
* Once an in-stock button is available, the bot will click it automatically while also opening a page on your default browser just in case
* Since Best Buy works by having a queue, the bot will continually check the button to turn yellow without refreshing, and click it once it does
* You will get an alert both when it is in stock, and when it is added to cart. I'd recommend using the in-stock alert to do this on an normal browser as backup


