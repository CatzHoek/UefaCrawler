from CountryStatistic import CountryStatistic

playerPerCountry = CountryStatistic('sweden.json')
for entry in sorted(playerPerCountry.result):
	print entry, playerPerCountry.result[entry]