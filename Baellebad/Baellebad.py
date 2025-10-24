import operator


class Unterricht:
	def __init__(self, Class, Day, Start, End, BallsNeeded):
		self.Class = Class
		self.Day = Day	
		self.Start = int(Start)
		self.End = int(End)
		self.BallsNeeded = int(BallsNeeded)

	def __str__(self):
		return f"{self.BallsNeeded} zwischen {self.Start} und {self.End}"


# Berechnet die Stunden in denen die Bälle benötigt werden
def getHours(start, end):
	c = start
	hours = []
	while c <= end:
		hours.append(c)
		c = c + 1 
	return hours

def isSport(name):
	if name[0].isdigit():
		return True
	elif name.startswith("SP")  or name.startswith("sp"):
		return True
	else:
		return False


def getData(file):
	with open('data/' + file) as f:
		lines = f.readlines()
		del lines[0] # Erste Zeile mit dem Jahrgang, ig das bringt erstmal nix

		classes = []
		timeStamps = {}

		# Einlesen der Daten in die Klasse, ich hab ja gaarkeinen Bock mit indices zu arbeiten
		for line in lines:
			tempClass = line.split(" ")
			classes.append(Unterricht(tempClass[0],tempClass[1],tempClass[2],tempClass[3],tempClass[4].rstrip()))

		for item in classes:
			hours = getHours(item.Start, item.End)
			for hour in hours:
				if isSport(item.Class):
					lastVal = timeStamps.get(hour)
					if lastVal == None: lastVal = 0
					timeStamps[hour] = lastVal + item.BallsNeeded
		print("Gesamtzahlen: " + str(timeStamps))
		maxValue = max(timeStamps.values())
		maxHour = max(timeStamps, key=timeStamps.get)
		print("Die Schule braucht höchstens " + str(maxValue) + " Bälle um " + str(maxHour) + " Uhr!")
		return timeStamps