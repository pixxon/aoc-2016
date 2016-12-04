# Check if length of edges stored in the list are valid.
def checkTriangle(edges):
	if (type(edges) is not list or len(edges) != 3):
		raise ValueError('Parameter must be a list containing the 3 edges!')
	a, b, c = edges
	return a + b > c and a + c > b and b + c > a

# Solution for first part.
def first():
	count = sum(1 for line in open('input.txt') if checkTriangle(list(map(lambda str: int(str), line.split()))))
	
	print('\nFirst part:')
	print('\tNumber of triangles: ' + str(count))

import itertools
# Solution for second part.
def second():
	count = 0
	with open('input.txt') as f:
		for line1,line2,line3 in itertools.zip_longest(*[f]*3):
			sides = list(map(lambda str: int(str), line1.split() + line2.split() + line3.split()))
			count += checkTriangle(sides[0::3])
			count += checkTriangle(sides[1::3])
			count += checkTriangle(sides[2::3])
	
	print('\nSecond part:')
	print('\tNumber of triangles: ' + str(count))

if __name__ == '__main__':
	first()
	second()