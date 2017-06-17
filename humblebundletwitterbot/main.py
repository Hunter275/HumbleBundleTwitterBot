# Hunter Thornsberry http://www.adventuresintechland.com
# HumbleBundleTwitterBot - Searches for humblebundle key urls and attempts to redeem them

import twitter
import re
import mechanize
import httplib
import urlparse
import ssl
import time
import urllib
import requests.packages.urllib3
import logging

# User Settings
email = "your@email.com"
user_consumer_key = "KEY"
user_consumer_secret = "KEY"
user_access_token_key = "KEY"
user_access_token_secret = "KEY"

if email == "your@email.com" or user_consumer_key == "KEY" or user_consumer_secret == "KEY" or user_access_token_key == "KEY" or user_access_token_secret == "KEY":
    print "Please edit main.py and input your user settings"
    exit()

# Setup logging
logging.basicConfig(filename='log.txt', format="%(asctime)s %(message)s", level=logging.INFO)

# Disable URL warning (known issues with HTTPS)
requests.packages.urllib3.disable_warnings()

# Make sure we don't try the same URL twice
previousURL = ""

def main():
    global previousURL

    # You'll need your own API keys (http://apps.twitter.com)
    api = twitter.Api(consumer_key=user_consumer_key,
                      consumer_secret=user_consumer_secret,
                      access_token_key=user_access_token_key,
                      access_token_secret=user_access_token_secret)

    # Get the Twitter API results, count=1
    results = api.GetSearch("humblebundle.com?gift", result_type="recent", count=1)

    # Turn this list into a string to parse it
    results = str(results)

    # Grab any URL from the status
    url = re.search("(?P<url>https?://[^\s]+)", results).group("url")

    # Concatenate the URL if the URL is the last bit of text, which has trailing characters from the API
    if url[len(url) - 3:] == '")]' or url[len(url) - 3:] == "')]":
        url = url[:-3]

    # Twitter's API shortens all URLs as t.co domains, this grabs the full domain behind it
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnection(parsed.netloc)
    h.request('HEAD', parsed.path)
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        url = response.getheader('Location')
    else:
        url = url

    if url == previousURL:
        print "Already tried this URL:", url
        logging.info("Already tried this URL: " + url)
    else:
        # Try to claim the gift
        print "Trying '" + url + "'"
        logging.info("Trying '" + url + "'")
        previousURL = url

        # Use mechanize to populate the two email fields and submit the form
        # Note: Working on bug fixes in this location
        try:
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.open(url)
            br.select_form(id="gift-redeem")
            br["email"] = email
            br.form.find_control(id="email-confirm").__setattr__("value", email)
            br.submit()
        except Exception as exp:
            if str(exp) != "<urlopen error [Errno 8] _ssl.c:507: EOF occurred in violation of protocol>": # Known request issue, works regardless
                logging.debug(str(exp))
            pass

while True:
    main()
    time.sleep(60)
