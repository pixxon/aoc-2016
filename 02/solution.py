# Simple class to store position on 2D grid.
class Position:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	
	def move(self, direction):
		if direction == 'D':
			return Position(self.x + 1, self.y)
		if direction == 'U':
			return Position(self.x - 1, self.y)
		if direction == 'R':
			return Position(self.x, self.y + 1)
		if direction == 'L':
			return Position(self.x, self.y - 1)
		raise ValueError('Direction must be U, D, L or R!')

# Common interface for different KeyPads.
class KeyPad:
	def moveFinger(self, direction):
		raise NotImplementedError('You must override this method!')
	
	def getCurrentDigit(self):
		raise NotImplementedError('You must override this method!')

# KeyPad implementation for good old 3 by 3 pads with numbers.
class SimpleKeyPad(KeyPad):
	def __init__(self, position = Position(1, 1)):
		self.__pos = position
	
	def moveFinger(self, direction):
		next = self.__pos.move(direction)
		if self.__inRange(next):
			self.__pos = next
	
	def getCurrentDigit(self):
		return str(3 * self.__pos.x + self.__pos.y + 1)
	
	def __inRange(self, position):
		return (position.x >= 0 and position.x <= 2 and position.y >=0 and position.y <= 2)

# Tricky bathroom keypads implementation.
class ComplexKeyPad(KeyPad):
	__decodeTable = None
	
	def __init__(self, position = Position(0, -2)):
		ComplexKeyPad.__decodeTable = ComplexKeyPad.__generateTable()
		self.__pos = position
	
	def moveFinger(self, direction):
		next = self.__pos.move(direction)
		if self.__inRange(next):
			self.__pos = next
	
	def getCurrentDigit(self):
		return ComplexKeyPad.__decodeTable[self.__pos.x][self.__pos.y]
	
	def __inRange(self, position):
		return ((abs(position.x) + abs(position.y)) <= 2)
	
	# Couldn't think of a better way to map the values.
	@staticmethod
	def __generateTable():
		if (ComplexKeyPad.__decodeTable != None):
			return ComplexKeyPad.__decodeTable
		
		table = dict()
		table[-2] = { 0 : '1'}
		table[-1] = {-1 : '2',  0 : '3', 1 : '4'}
		table[ 0] = {-2 : '5', -1 : '6', 0 : '7', 1 : '8', 2 : '9'}
		table[ 1] = {-1 : 'A',  0 : 'B', 1 : 'C'}
		table[ 2] = { 0 : 'D'}
		
		return table

# Solving first problem.
def first():
	code = ''
	for line in open('input.txt').readlines():
		numpad = SimpleKeyPad()
		
		for direction in line[:-1]:
			numpad.moveFinger(direction)
			
		code += numpad.getCurrentDigit()
	
	print('\nFirst part:')
	print('\tCode: ' + code,)

# Solving second problem.
def second():
	code = ''
	numpad = ComplexKeyPad()
	for line in open('input.txt').readlines():
		
		for direction in line[:-1]:
			numpad.moveFinger(direction)
			
		code += numpad.getCurrentDigit()
		
	print('\nSecond part:')
	print('\tCode: ' + code)

if __name__ == '__main__':
	first()
	second()
