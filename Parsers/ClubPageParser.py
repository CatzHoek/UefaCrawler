#!/usr/bin/python

import HTMLParser
import re

class ClubPageParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.setFalse()
		self.in_playername = False
		self.result = []
		self.player = {}

	def setFalse(self):
		self.in_gkp = False
		self.in_def = False
		self.in_mid = False
		self.in_stk = False

	def getCurrentPosition(self):
		if self.in_gkp:
			return 'gkp'
		elif self.in_def:
			return 'def'
		elif self.in_mid:
			return 'mid'
		elif self.in_stk:
			return 'stk'

	def handle_starttag(self, tag, attrs):
		if tag == 'div':
			for key, value in attrs:
				if key == 'id' and value == 'gkp':
					self.setFalse()
					self.in_gkp = True
				if key == 'id' and value == 'def':
					self.setFalse()
					self.in_def = True
				if key == 'id' and value == 'mid':
					self.setFalse()
					self.in_mid = True
				if key == 'id' and value == 'stk':
					self.setFalse()
					self.in_stk = True

		if tag == 'a':
			if self.in_playername:
				for key, value in attrs:
					if key == 'href':	
						pattern = re.compile("(.*?)(\d+)")
						match = re.match(pattern, value)
						self.player['id'] = match.group(2)

		if tag == 'tr':
			for key, value in attrs:
				if key == 'class' and value == 'player':
					self.in_player_tr = True

		if tag == 'td':
			for key, value in attrs:
				if key == 'class':
					for v in value.rsplit():
						if v == 'playername':
							self.in_playername = True
		
	def handle_endtag(self, tag):
		if tag == 'div':
			self.setFalse()
		if tag == 'td':
			self.in_playername = False;
			
	def handle_data(self, data):
		if self.in_playername:
			self.player['name'] = data
			self.player['position'] = self.getCurrentPosition()
			self.result.append(self.player)
			self.player = {}
			
	def get(self):
		return self.result