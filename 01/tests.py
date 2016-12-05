import unittest
from solution import Direction, Position, first, second
import os
import sys

class TestDirectionTurn(unittest.TestCase):
	def testLeftTurn(self):
		direction = Direction.NORTH
		direction = Direction.turn(direction, 'L')
		self.assertEqual(direction, Direction.WEST)
		direction = Direction.turn(direction, 'L')
		self.assertEqual(direction, Direction.SOUTH)
		direction = Direction.turn(direction, 'L')
		self.assertEqual(direction, Direction.EAST)
		direction = Direction.turn(direction, 'L')
		self.assertEqual(direction, Direction.NORTH)
	
	def testRightTurn(self):
		direction = Direction.NORTH
		direction = Direction.turn(direction, 'R')
		self.assertEqual(direction, Direction.EAST)
		direction = Direction.turn(direction, 'R')
		self.assertEqual(direction, Direction.SOUTH)
		direction = Direction.turn(direction, 'R')
		self.assertEqual(direction, Direction.WEST)
		direction = Direction.turn(direction, 'R')
		self.assertEqual(direction, Direction.NORTH)
	
	def testInvalidTurn(self):
		self.assertRaises(ValueError, Direction.turn, Direction.NORTH, 'U')
		self.assertRaises(ValueError, Direction.turn, Direction.NORTH, 5)
		self.assertRaises(ValueError, Direction.turn, Direction.NORTH, None)
	
	def testInvalidDirection(self):
		self.assertRaises(ValueError, Direction.turn, 5, 'L')
		self.assertRaises(ValueError, Direction.turn, 'north', 'L')
		self.assertRaises(ValueError, Direction.turn, None, 'L')
	
	def testNormal(self):
		direction = Direction.NORTH
		direction = Direction.turn(direction, 'L')
		direction = Direction.turn(direction, 'R')
		self.assertEqual(direction, Direction.NORTH)
		direction = Direction.turn(direction, 'L')
		direction = Direction.turn(direction, 'L')
		self.assertEqual(direction, Direction.SOUTH)
		direction = Direction.turn(direction, 'R')
		self.assertEqual(direction, Direction.WEST)

class TestPosition(unittest.TestCase):
	def testEquals(self):
		self.assertEqual(Position(0, 0), Position(0, 0))
		self.assertEqual(Position(1, 6), Position(1, 6))
		self.assertEqual(Position(-6, 2), Position(-6, 2))
		self.assertNotEqual(Position(0, 0), Position(0, 5))
		self.assertNotEqual(Position(0, 0), Position(5, 0))
		self.assertNotEqual(Position(1, 1), Position(2, 2))
		self.assertNotEqual(Position(-1, 3), Position(3, -1))
	
	def testCopy(self):
		pos1 = Position(5, 3)
		pos2 = Position.copy(pos1)
		self.assertEqual(pos1, pos2)
		pos1.x = 3
		self.assertNotEqual(pos1, pos2)
	
	def testDistance(self):
		pos1 = Position(5, 3)
		pos2 = Position(5, 3)
		pos3 = Position(2, 3)
		pos4 = Position(5, 7)
		pos5 = Position(10, -4)
		
		self.assertEqual(pos1.distanceFrom(pos2), 0)
		self.assertEqual(pos1.distanceFrom(pos3), 3)
		self.assertEqual(pos1.distanceFrom(pos4), 4)
		self.assertEqual(pos1.distanceFrom(pos5), 12)
		self.assertEqual(pos4.distanceFrom(pos5), 16)
	
	def testStr(self):
		pos1 = Position(1, 1)
		pos2 = Position(-4, 2)
		
		self.assertEqual(str(pos1), '(x: 1, y: 1)')
		self.assertEqual(str(pos2), '(x: -4, y: 2)')

# Check the solution on provided examples.
class TestSolutions(unittest.TestCase):
	def testFirst(self):
		self.assertEqual(first('R2, L3'), 5)
		self.assertEqual(first('R2, R2, R2'), 2)
		self.assertEqual(first('R5, L5, R5, R3'), 12)
	
	def testSecond(self):
		self.assertEqual(second('R8, R4, R4, R8'), 4)

if __name__ == '__main__':
	# Turning off stdout for running the tests.
	tmp = sys.stdout
	f = open(os.devnull, 'w')
	sys.stdout = f
	
	unittest.main()
	
	# Turning it back on.
	sys.stdout = tmp