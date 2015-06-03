#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import re
import collections
import json
import HTMLParser
from pymongo import MongoClient
html = HTMLParser.HTMLParser()
conn = MongoClient()
db = conn['commentsSentiment']
cardInfoDB = db.cardDataComplete
print cardInfoDB.count()