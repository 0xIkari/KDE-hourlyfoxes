#!/usr/bin/env python3
import sys
import os
import urllib3
import chardet
import twint

username = sys.argv[1]

os.remove("pictures.csv")

c = twint.Config()
c.Username = username
c.Custom["tweet"] = ["date","time","photos"]
c.Limit = 20 #Minimum for Twint
c.Output = "pictures.csv"
c.Store_csv = True

twint.run.Search(c)

#Post Processing
lines = []
with open(r"pictures.csv", 'r') as fp:
    lines = fp.readlines()

with open(r"pictures.csv", 'w') as fp:
    for number, line in enumerate(lines):
        if number in [1]: #Pull only the most recent image
            line = line[22:-3]
            url = line
            urllib.request.urlretrieve(url, "desktop.jpg")
            print(line)
            fp.write(line)

