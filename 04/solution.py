# Unpack sector from tuple.
def getSector(checksum, sector, code):
	return sector

# Unpack code from tuple.
def getCode(checksum, sector, code):
	return code

# Maybe using regex would be better.
def parseLine(line):
	return (line[-7:][:5], int(line[-11:][:3]), line[:-11].replace('-', ''))

# Check if code matches the checksum.
def isValid(checksum, sector, code):
	import collections
	
	tops = [(-n,c) for c,n in collections.Counter(code).most_common()]
	return ''.join(c for n,c in sorted(tops)).startswith(checksum)

# Generate a table to map characters. Based on sectorID.
def decryptTable(sector):
	import string
	
	letters = string.ascii_lowercase
	cropped = sector % len(string.ascii_lowercase)
	return str.maketrans(letters, letters[cropped:] + letters[:cropped])

# Solution for first problem.
def first():
	count = sum(getSector(*parseLine(line)) for line in open('input.txt') if isValid(*parseLine(line)))
	
	print('\nFirst part:')
	print('\tSum of sector ID\'s of valid rooms: ' + str(count))

# Solution for second problem.
def second():
	sector = next(getSector(*parseLine(line)) for line in open('input.txt') if 'north' in getCode(*parseLine(line)).translate(decryptTable(getSector(*parseLine(line)))))
	
	print('\nSecond part:')
	print('\tNorth pole sector ID: ', sector)

if __name__ == '__main__':
	first()
	second()
