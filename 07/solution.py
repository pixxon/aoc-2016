def isABBA(abba):
	return (len(abba) == 4 and abba[0] != abba[1] and abba[0] == abba[3] and abba[1] == abba[2])

def isABA(aba):
	return (len(aba) == 3 and aba[0] != aba[1] and aba[0] == aba[2])

def matchPair(aba, bab):
	return (len(aba) == len(bab) == 3 and aba[0] == aba[2] == bab[1] and aba[1] == bab[0] == bab[2])

import re
def findOutsideBracket(str):
	return re.findall('(?:^|\])([a-z]+)(?:$|\[)', str)

def findInsideBracket(str):
	return re.findall('\[([a-z]+)\]', str)

class WordListIterable(list):
	def __init__(self, list, cond, wordLen):
		self.__list = list
		self.__cond = cond
		self.__wordLen = wordLen
		self.__listIndex = 0
		self.__wordIndex = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if len(self.__list) <= self.__listIndex:
			raise StopIteration
		
		if len(self.__list[self.__listIndex]) < (self.__wordIndex + self.__wordLen):
			self.__listIndex += 1
			self.__wordIndex = 0
			return self.__next__()
		
		word = self.__list[self.__listIndex][self.__wordIndex:(self.__wordIndex + self.__wordLen)]
		self.__wordIndex += 1
		if self.__cond(word):
			return word
		else:
			return self.__next__()

def supportTLS(str):
	inside = findInsideBracket(str)
	matchInside = next((True for bab in WordListIterable(inside, isABBA, 4)), False)
	
	outside = findOutsideBracket(str)
	matchOutside = next((True for bab in WordListIterable(outside, isABBA, 4)), False)
	
	return (not matchInside and matchOutside)

def supportSSL(str):
	inside = findInsideBracket(str)
	outside = findOutsideBracket(str)
	
	for aba in WordListIterable(outside, isABA, 3):
		match = next((True for bab in WordListIterable(inside, isABA, 3) if matchPair(aba, bab)), False)
		if match:
			return True
	return False

def first(input):
	count = sum([1 for ip in input if supportTLS(ip)])
	
	print('\nFirst part:')
	print('\tNumber of IPs: ' + str(count))
	
	return count

def second(input):
	count = sum([1 for ip in input if supportSSL(ip)])
	
	print('\nSecond part:')
	print('\tNumber of IPs: ' + str(count))
	
	return count

if __name__ == '__main__':
	first(open('input.txt'))
	second(open('input.txt'))
