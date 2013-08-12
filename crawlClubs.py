#!/usr/bin/python

#import urllib
#import cookielib
import mechanize
import json

from Parsers import SeriesPageParser
from Parsers import ClubPageParser
from Parsers import PlayerPageParser

class FifaCom:
	def __init__(self):
		self.browser = mechanize.Browser()
		self.body = ''
		
	def open(self, url):
		self.response = self.browser.open(url)
		self.body = self.response.get_data();
		self.body = unicode(self.body.decode('utf-8'))

#find clubs from country page, edit this url to change league
fifapage = FifaCom()
url = 'http://www.uefa.com/memberassociations/association=fra/index.html'
fifapage.open(url)

parser = SeriesPageParser.SeriesPageParser()
parser.feed(fifapage.body)
clubs = parser.get()


for club in clubs:
	url = "http://www.uefa.com/teamsandplayers/teams/club=%s/domestic/index.html" % (club['id'])
	fifapage.open(url)
	parser = ClubPageParser.ClubPageParser()
	parser.feed(fifapage.body)
	players = parser.get()
	club['players'] = []
	for player in players:
		#some players have no page on uefa.com, skip those :(
		if 'id' not in player:
			player['country'] = 'unknown'
			club['players'].append(player)
			continue

		url = "http://www.uefa.com/teamsandplayers/players/player=%s/profile/index.html" % (player['id'])
		fifapage.open(url)
		parser = PlayerPageParser.PlayerPageParser()
		parser.feed(fifapage.body)
		player['country'] = parser.get()
		club['players'].append(player)

	#break #for test purposes

print json.dumps(clubs)