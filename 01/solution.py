# This class is used to represent directions in our program
class Direction:
	NORTH = 0
	WEST = 1
	SOUTH = 2
	EAST = 3
	
	def turn(direction, turn):
		if (turn != 'L' and turn != 'R'):
			raise ValueError('Turn must be L or R!')
		
		# Bit hackish
		if (direction < 0 or direction > 3):
			raise ValueError('Direction must be NORTH, WEST, SOUTH or EAST!')
	
		if turn == 'L':
			return (direction + 1) % 4
			
		if turn == 'R':
			return (direction + 3) % 4

# Simple class to store position in a 2D grid.
class Position:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
		
	@staticmethod
	def copy(position):
		return Position(position.x, position.y)
		
	def move(self, direction, distance = 1):
		if (distance < 0):
			raise ValueError('Distance must be a positive value!')
	
		if direction == Direction.NORTH:
			self.x += distance
		elif direction == Direction.SOUTH:
			self.x -= distance
		elif direction == Direction.WEST:
			self.y += distance
		elif direction == Direction.EAST:
			self.y -= distance
		else:
			raise ValueError('Invalid direction!')
			
	def distanceFrom(self, other):
		if type(other) is not self.__class__:
			raise ValueError('Parameter can be only Position!')
			
		return abs(self.x - other.x) + abs(self.y - other.y)
		
	def __str__(self):
		return '(x: ' + str(self.x) + ', y: ' + str(self.y) + ')'
		
	def __eq__(self, other):
		if type(other) is not self.__class__:
			raise ValueError('Parameter can be only Position!')
		
		return (self.x == other.x and self.y == other.y)
		
# Solving the first problem.
def first():
	startPos = Position(0, 0)
	currentPos = Position.copy(startPos)
	direction = Direction.NORTH

	for movement in open('input.txt').readline().split(', '):
		direction = Direction.turn(direction, movement[:1])
		currentPos.move(direction, int(movement[1:]))
			
	print('\nFirst part:')
	print('\tEnd point: ' + str(currentPos))
	print('\tDistance: ', currentPos.distanceFrom(startPos))
	
# Solving the second problem.
def second():
	startPos = Position(0, 0)
	currentPos = Position.copy(startPos)
	direction = Direction.NORTH
	
	history = list()
	history.append(Position.copy(currentPos))

	found = False
	for movement in open('input.txt').readline().split(', '):
		direction = Direction.turn(direction, movement[:1])
		
		for i in range(int(movement[1:])):
			currentPos.move(direction)
				
			if currentPos in history:
				found = True
				break
				
			history.append(Position.copy(currentPos))
				
		if found:
			break
	
	print('\nSecond part:')
	print('\tFirst point visited twice: ' + str(currentPos))
	print('\tDistance: ', currentPos.distanceFrom(startPos))

if __name__ == '__main__':
	first()
	second()
