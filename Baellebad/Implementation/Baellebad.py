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
		del lines[0] # die erste Zeile ist nicht relevant für diesen Zweck

		classes = []

		days = {"Montag": {}, "Dienstag" : {}, "Mittwoch": {}, "Donnerstag" : {},  "Freitag" : {}} # dictionary of Weekdays, with their corresponding Timestamps


		for line in lines:
			tempClass = line.split(" ")
			classes.append(Unterricht(tempClass[0],tempClass[1],tempClass[2],tempClass[3],tempClass[4].rstrip()))

		for item in classes:
			hours = getHours(item.Start, item.End)
			day_time_stamps = days[item.Day]
			for hour in hours:
				if isSport(item.Class):
					lastVal = day_time_stamps.get(hour)
					if lastVal is None: lastVal = 0
					day_time_stamps[hour] = lastVal + item.BallsNeeded
			days[item.Day] = day_time_stamps

		maxBalls = 0
		maxHour = 0
		maxDay = ""
		graphDict = {}
		# calculate maximum usage
		for dayKey, day in days.items():  # Use .items() to get both key and value
			if len(day.values()) > 0:
				maxValue = max(day.values())
				if maxValue > maxBalls:
					maxBalls = maxValue
					maxHour = max(day, key=day.get)  # gets the hour corresponding to max value
					maxDay = dayKey  # stores the day name

		for day, hours in days.items():
			for hour, value in hours.items():
				graphDict[f"{day[0] + day[1]} {hour}"] = value
		return maxValue, maxHour, maxDay, graphDict