class Bot:
	signal = None

	bots = list()
	outputs = dict()
	
	def __init__(self, name, lowName, highName):
		self.name = name
		self.lowName = lowName
		self.highName = highName
		
		self.first = None
		self.second = None
		
		Bot.bots.append(self)
	
	def add(self, value):
		if self.first == None:
			self.first = value
			return
			
		self.second = value
		
		self.compare()
	
	def compare(self):
		low, high = (self.first, self.second) if (self.first < self.second) else (self.second, self.first)
		
		self.first = None
		self.second = None
		
		if Bot.signal is not None:
			Bot.signal(self.name, low, high)
		
		Bot.send(self.lowName, low)
		Bot.send(self.highName, high)
		
	@staticmethod
	def send(name, value):
		if 'output' in name:
			Bot.outputs[name] = value
			return
		for bot in Bot.bots:
			if bot.name == name:
				bot.add(value)
				return

import re
def processFile(input):
	config = re.compile('(?P<name>bot [0-9]+) gives low to (?P<lowName>(?:bot|output) [0-9]+) and high to (?P<highName>(?:bot|output) [0-9]+)')
	msg = re.compile('value (?P<value>[0-9]+) goes to (?P<name>bot [0-9]+)')
	
	values = list()
	configs = list()
	
	for line in input:
		if 'value' in line:
			values.append(msg.match(line).groupdict())
		else:
			configs.append(config.match(line).groupdict())
	
	return values, configs
	

def first(input):
	first.result = None
	
	def checker(name, low, high):
		if low == 17 and high == 61:
			first.result = name

	Bot.signal = checker
	
	values, configs = processFile(input)
	
	for config in configs:
		Bot(config['name'], config['lowName'], config['highName'])
	
	for value in values:
		Bot.send(value['name'], int(value['value']))
		
	Bot.signal = None
	
	print('\nFirst part:')
	print('\tComparing bot: ' + first.result)
	
	return first.result
	
def second(input):	
	values, configs = processFile(input)
	
	for config in configs:
		Bot(config['name'], config['lowName'], config['highName'])
	
	for value in values:
		Bot.send(value['name'], int(value['value']))
	
	value = Bot.outputs['output 0'] * Bot.outputs['output 1'] * Bot.outputs['output 2']
	
	print('\nSecond part:')
	print('\tSum of outputs: ' + str(value))
	
	return value

if __name__ == '__main__':
	first(open('input.txt'))
	second(open('input.txt'))