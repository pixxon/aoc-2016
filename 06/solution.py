from collections import Counter

class ColumnIterator:
	def __init__(self, table, column):
		self.__table = table
		self.__column = column
		self.__row = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if len(self.__table) <= self.__row:
			raise StopIteration
		
		self.__row += 1
		return self.__table[self.__row - 1][self.__column]

def first(data):
	if len(data) < 1:
		return
	msg = ''.join([Counter(ColumnIterator(data, column)).most_common()[0][0] for column in range(len(data[0]))])
	
	print('\nFirst part:')
	print('\tMessage: ' + msg)
	
	return msg

def second(data):
	if len(data) < 1:
		return
	msg = ''.join([Counter(ColumnIterator(data, column)).most_common()[-1][0] for column in range(len(data[0]))])
	
	print('\nSecond part:')
	print('\tMessage: ' + msg)
	
	return msg

if __name__ == '__main__':
	data = open('input.txt').read().splitlines()
	first(data)
	second(data)