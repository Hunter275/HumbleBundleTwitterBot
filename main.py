# Hunter Thornsberry http://www.adventuresintechland.com
# HumbleBundleTwitterBot - Searches for humblebundle key urls and attempts to redeem them

import twitter # https://github.com/bear/python-twitter
import re

# Put your keys here
api = twitter.Api(consumer_key="KEY",
                  consumer_secret="KEY",
                  access_token_key="KEY",
                  access_token_secret="KEY")

# Search results, limited to 1 (count=1)
results = api.GetSearch("humblebundle.com?gift", result_type="recent", count=1)

# Parse the result for the url minus the last 3 character (left overs from the formatting of twitter results)
parsed = re.search("(?P<url>https?://[^\s]+)", results).group("url")[:-3]

#print the URL
print parsed
