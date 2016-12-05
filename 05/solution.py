import hashlib

class HashGenerator:
	def __init__(self, salt):
		self.__salt = salt
		self.__counter = 0
	
	def next(self, condition):
		hash = hashlib.md5((self.__salt + str(self.__counter)).encode('utf8')).hexdigest()
		self.__counter += 1
		while(not condition(hash)):
			hash = hashlib.md5((self.__salt + str(self.__counter)).encode('utf8')).hexdigest()
			self.__counter += 1
		return hash

def first():
	generator = HashGenerator('abbhdwsy')
	code = list('--------')
	for i in range(8):
		hash = generator.next(lambda x : x.startswith('00000'))
		code[i] = hash[5]
		
	print('\nFirst part:')
	print('\tCode: ' + ''.join(code))

def second():
	generator = HashGenerator('abbhdwsy')
	code = list('--------')
	for i in range(8):
		hash = generator.next(lambda x : x.startswith('00000') and int(x[5], 16) < 8 and code[int(x[5])] == '-')
		code[int(hash[5])] = hash[6]
	
	print('\nSecond part:')
	print('\tCode: ' + ''.join(code))

if __name__ == '__main__':
	first()
	second()