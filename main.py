# Hunter Thornsberry http://www.adventuresintechland.com
# HumbleBundleTwitterBot - Searches for humblebundle key urls and attempts to redeem them

import twitter # https://github.com/bear/python-twitter
import re
import mechanize
import httplib
import urlparse
import ssl

# Set your email address
email = "your@email.com"

api = twitter.Api(consumer_key="KEY",
                  consumer_secret="KEY",
                  access_token_key="KEY",
                  access_token_secret="KEY")

# Get the Twitter API results, count=1
results = api.GetSearch("humblebundle.com?gift", result_type="recent", count=1)

# Turn this list into a string to parse it
results = str(results)

# Grab any URL from the status
url = re.search("(?P<url>https?://[^\s]+)", results).group("url")[:-3]

# Twitter's API shortens all URLs as t.co domains, this grabs the full domain behind it
parsed = urlparse.urlparse(url)
h = httplib.HTTPConnection(parsed.netloc)
h.request('HEAD', parsed.path)
response = h.getresponse()
if response.status/100 == 3 and response.getheader('Location'):
    url = response.getheader('Location')
else:
    url = url

# Try to claim the gift
print "Trying '" + url + "'"

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
    print type(exp)
    print exp
