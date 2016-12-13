import io

def peek(f, length=1):
    pos = f.tell()
    data = f.read(length)
    f.seek(pos)
    return data

class Tokenizer:
	__begin = '('
	__end = ')'
	__split = 'x'

	def __init__(self, instream):
		self.__instream = instream
		
	def __iter__(self):
		return self
		
	def __next__(self):
		c = peek(self.__instream)
		
		if not c:
			raise StopIteration
			
		if c == '(':
			c = self.__instream.read(1)
			c = peek(self.__instream)
			
			repAmount = int(self.__readUntil(Tokenizer.__split))
			
			c = self.__instream.read(1)
			c = peek(self.__instream)
			
			repCount = int(self.__readUntil(Tokenizer.__end))
			
			c = self.__instream.read(1)
			c = peek(self.__instream)
			
			return {'name' : 'repeat', 'amount' : repAmount, 'count' : repCount}
		else:
			data = self.__readUntil(Tokenizer.__begin)			
			return {'name' : 'data', 'value' : data}
			
	def __readUntil(self, char):
		data = ''
		c = peek(self.__instream)
		while c and c != char:
			c = self.__instream.read(1)
			data += c
			c = peek(self.__instream)
		return data
			
def simpleDecomp(stream):
	result = ''
	for token in Tokenizer(stream):
		if token['name'] == 'repeat':
			data = stream.read(token['amount'])
			result += data.strip() * token['count']
		if token['name'] == 'data':
			result += token['value'].strip()
	return result

def recursiveDecomp(stream):
	sum = 0
	for token in Tokenizer(stream):
		if token['name'] == 'repeat':
			data = stream.read(token['amount']).strip()
			data = recursiveDecomp(io.StringIO(data))
			sum += data * token['count']
		if token['name'] == 'data':
			sum += len(token['value'].strip())
	return sum


def first(input):
	decomp = simpleDecomp(input)
	
	print('\nFirst part:')
	print('\tDecompressed length of file: ' + str(len(decomp)))
	
	return len(decomp)
	
def second(input):
	decomp = recursiveDecomp(input)
	
	print('\nSecond part:')
	print('\tDecompressed length of file: ' + str(decomp))
	
	return decomp

if __name__ == '__main__':
	first(open('input.txt'))
	second(open('input.txt'))
