#!/usr/bin/python

import HTMLParser
import re

class PlayerPageParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.result = ''
		self.in_details = False

	def handle_starttag(self, tag, attrs):
		if tag == 'div':
			for key, value in attrs:
				if key == 'class' and value == 'HeaderDetails':
					self.in_details = True

		if self.in_details:
			if tag == 'img':
				for key, value in attrs:
					if key == 'alt':
						self.result = value

					#if key == 'src':
					#	print 'flag', value

		
	def handle_endtag(self, tag):
		if tag == 'div':
			self.in_details = False
			
	def get(self):
		return self.result