# HumbleBundle Twitter Bot

A bot that attempts to grab Tweeted humblebundle game links and tries to add them to your inventory.

Notice: I don't use the Twitter Streaming API because Twitter shortens all URLs to t.co/ and it is impossible to see what's behind them to find the humblebundle links, and filtering happens after the urls are shortened. As a result, the Twitter Search API is used to find tweets that originally contained the "humblebundle.com/gift?key=" text.

---
To-Do
1. Make the logger not log so many "Already tried this URL..." messages
