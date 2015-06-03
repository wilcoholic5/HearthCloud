#!/usr/bin/python
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib2
import time
import re

i = 3200
cards = []
for num in range(1, i):
		webpage = urllib2.Request('http://www.hearthhead.com/card='+str(num))
		try:
			contents = urllib2.urlopen(webpage)
		except urllib2.HTTPError as e:
			if e.code == 404:
				print 'card ' + str(num) + ' does not exist'
				continue
		print 'adding ' + str(num)
		cards.append(num)
		if num > 511:
			print cards
		
print cards
#soup = BeautifulSoup(browser.page_source)
#
#print soup.prettify()
