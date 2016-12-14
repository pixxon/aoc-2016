import re
import hashlib
import itertools

class CodeCache:
	def __init__(self, salt, generator):
		self.salt = salt
		self.cache = dict()
		self.generator = generator
		
	def generate(self, number):
		if number in self.cache:
			return self.cache[number]
			
		code = self.generator(self.salt + str(number))
		self.cache[number] = code
		return code
			
def first(salt):
	reg = re.compile('.*(.)\\1{2}.*')
	
	def myMD5(code):
		m = hashlib.md5()
		m.update(code.encode('utf-8'))
		return m.hexdigest()
		
	cache = CodeCache(salt, myMD5)
	count, i = 0, 0
	while count < 65:
		code = cache.generate(i)
		match = reg.match(code)
		while not match:
			i += 1
			code = cache.generate(i)
			match = reg.match(code)
		
		found = False
		for j in range(i + 1, i+1000):
			code = cache.generate(j)
			if (match.groups()[0] * 5) in code:
				found = True
				break
		
		count, i = count + found, i + 1
			
	print('\nFirst part:')
	print('\tIndex of 64th valid code: ' + str(i - 1))
	
	return (i - 1)
		

def second(salt):
	reg = re.compile('.*(.)\\1{2}.*')
	
	def myMD5(code):
		for i in range(2017):
			m = hashlib.md5()
			m.update(code.encode('utf-8'))
			code = m.hexdigest()
		return code
		
	cache = CodeCache(salt, myMD5)
	count, i = 0, 0
	while count < 66:
		code = cache.generate(i)
		match = reg.match(code)
		while not match:
			i += 1
			code = cache.generate(i)
			match = reg.match(code)
		
		found = False
		for j in range(i + 1, i+1000):
			code = cache.generate(j)
			if (match.groups()[0] * 5) in code:
				found = True
				break
		
		count, i = count + found, i + 1
			
	print('\nSecond part:')
	print('\tIndex of 64th valid code: ' + str(i - 1))
	
	return (i - 1)

if __name__ == '__main__':
	first('ihaygndm')
	second('ihaygndm')
