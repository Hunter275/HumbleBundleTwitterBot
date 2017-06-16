# Hunter Thornsberry http://www.adventuresintechland.com
# A simple log writer

import datetime

def log(message):
    file = open("log.txt","a")
    file.write(str(datetime.datetime.now()) + " - " + message + "\n")
    file.close()
