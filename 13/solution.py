class Node:
	genCode = None

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.parent = None
	
	def distance(self, other):
		return abs(self.x - other.x) + abs(self.y - other.y)
	
	def neighbours(self):
		neigh = list()
		if self.x > 0 and Node(self.x - 1, self.y).__checkOpen():
			neigh.append(Node(self.x - 1, self.y))
		if self.y > 0 and Node(self.x, self.y - 1).__checkOpen():
			neigh.append(Node(self.x, self.y - 1))
		if Node(self.x + 1, self.y).__checkOpen():
			neigh.append(Node(self.x + 1, self.y))
		if Node(self.x, self.y + 1).__checkOpen():
			neigh.append(Node(self.x, self.y + 1))
		return neigh
			
	def __checkOpen(self):	
		value = self.x*self.x + 3*self.x + 2*self.x*self.y + self.y + self.y*self.y
		value += Node.genCode
		binCode = "{0:b}".format(value)
		sum = 0
		for bit in binCode:
			sum += int(bit)
		return not (sum % 2)
		
	def __eq__(self, other):
		if other == None:
			return False
		return self.x == other.x and self.y == other.y
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __str__(self):
		return '(x : ' + str(self.x) +'; y : ' + str(self.y) + ')'
	
	def __hash__(self):
		hash = 17;
		hash = ((hash + self.x) << 5) - (hash + self.x);
		hash = ((hash + self.y) << 5) - (hash + self.y);
		return hash;

class AStar:
	def __init__(self, h, limit = None):
		self.h = h
		self.limit = limit

	def buildPath(self, start, end):
		path = list()
		current = end
		while current != None:
			path.append(current)
			current = self.data[current]['p']
		return path
			
	def run(self, start, end):
		self.start = start
		self.end = end
	
		openNodes = list()
		openNodes.append(start)
		
		closedNodes = list()
		
		self.data = dict()
		self.data[start] = {'g' : 0, 'p': None}
		
		while openNodes:
			current = self.getLowestF(openNodes)
			
			if current == end:
				return self.buildPath(start, end), closedNodes
				
			if self.limit is not None and self.g(current) > self.limit:
				return [], closedNodes
			
			openNodes.remove(current)
			closedNodes.append(current)
						
			for node in current.neighbours():
				if node in closedNodes:
					continue
				
				nodeG = self.g(current) + current.distance(node)
				if node not in openNodes:
					openNodes.append(node)
				elif nodeG >= self.g(node):
					continue
					
				self.data[node] = {'g' : nodeG, 'p': current}
			
		return [], closedNodes
	
	def getLowestF(self, nodes):
		lowest = nodes[0]
		lowestF = self.f(lowest)
		for node in nodes:
			nodeF = self.f(node)
			if nodeF < lowestF:
				lowest = node
				lowestF = nodeF
		return lowest
	
	def f(self, node):
		return self.g(node) + self.h(node)
		
	def g(self, node):
		return self.data[node]['g']

def first(genCode):
	Node.genCode = genCode
	path, nodes = AStar(lambda x: 0).run(Node(1, 1), Node(31,39))
	
	print('\nFirst part:')
	print('\tLength of shortest path: ' + str(len(path) - 1))
	
	return len(path) - 1

def second(genCode):
	Node.genCode = genCode
	path, nodes = AStar(lambda x: 0, 50).run(Node(1, 1), Node(31,39))
	
	print('\nSecond part:')
	print('\tNumber of accessable tiles: ' + str(len(nodes)))
	
	return len(nodes) - 1

	
if __name__ == '__main__':
	inputCode = 1362
	first(inputCode)
	second(inputCode)