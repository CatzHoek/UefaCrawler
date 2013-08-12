#!/usr/bin/python

import HTMLParser
import re

class SeriesPageParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.in_tb_stand = False
		self.in_link = False
		self.result = []
		self.team = {}
		
	def handle_starttag(self, tag, attrs):
		if tag == 'table':
			for key, value in attrs:
				if key == 'class':
					for v in value.rsplit():
						if v == 'tb_stand':
							self.in_tb_stand = True

		if tag == 'a':
			if self.in_tb_stand:
				self.in_link = True
				for key, value in attrs:
					if key == 'href':	
						pattern = re.compile("(.*?)(\d+)")
						match = re.match(pattern, value)
						self.team['id'] = match.group(2)
		
	def handle_endtag(self, tag):
		if tag == 'table':
			self.in_tb_stand = False;
		if tag == 'a':
			self.in_link = False;
			
	def handle_data(self, data):
		if self.in_tb_stand:
			if self.in_link:
				self.team['name'] = data
				self.result.append(self.team)
				self.team = {}
			
	def get(self):
		return self.result