class Event:
	def __init__(self, attributes_array):
		self.date = attributes_array[0]
		self.time = attributes_array[1]
		
		self.opponent = attributes_array[3]
		self.location = attributes_array[4]
		self.notes = attributes_array[5]

	def __str__(self):
		return (self.date + " " + self.time + " " + self.opponent + " " + self.location)