#!/usr/bin/python

import json

class CountryStatistic:
	def __init__(self, filename):
		self.result = {}
		f = open(filename)
		self.data = json.load(f)
		f.close()
		self.count()

	def count(self):
		for item in self.data:
			for player in item['players']:
				if player['country'] not in self.countrycount:
					self.result[player['country']] = 1
				else:
					self.result[player['country']] = self.result[player['country']] + 1	

