#!/usr/bin/env python3

from urllib import request
#from bs4 import BeautifulSoup

with request.urlopen('https://repo1.maven.org/maven2/org/apache/commons/') as resp:
    index = resp.read().decode('utf-8')

print(index)
