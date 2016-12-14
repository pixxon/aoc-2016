import re

class Memory:
	def __init__(self, registers):
		self.__data = dict()
		for register in registers:
			self.__data[register] = 0
	
	def setValue(self, register, value):
		self.__data[register] = value
		
	def getValue(self, register):
		return self.__data[register]

class Program:
	def __init__(self, memory, code):
		lines = code.splitlines()
		
		self.__instructions = list()
		self.__instructions.append(re.compile('(?P<instr>cpy) (?P<val>[+-]?[0-9]+) (?P<reg>[abcd])'))
		self.__instructions.append(re.compile('(?P<instr>cpy) (?P<srcreg>[abcd]) (?P<desreg>[abcd])'))
		self.__instructions.append(re.compile('(?P<instr>inc) (?P<reg>[abcd])'))
		self.__instructions.append(re.compile('(?P<instr>dec) (?P<reg>[abcd])'))
		self.__instructions.append(re.compile('(?P<instr>jnz) (?P<val>[+-]?[0-9]+) (?P<pos>[+-]?[0-9]+)'))
		self.__instructions.append(re.compile('(?P<instr>jnz) (?P<reg>[abcd]) (?P<pos>[+-]?[0-9]+)'))
		
		self.__lines = list()
		for line in lines:
			self.__lines.append(self.__parse(line))
			
		self.__mem = memory
		
	def run(self):
		self.__curr = 0;
		while self.__curr < len(self.__lines):
			self.__process(self.__lines[self.__curr])
			self.__curr += 1
		
	def __process(self, instruction):
		if instruction['instr'] == 'cpy':
			if 'val' in instruction:
				self.__mem.setValue(instruction['reg'], int(instruction['val']))
			else:
				self.__mem.setValue(instruction['desreg'], self.__mem.getValue(instruction['srcreg']))
			return
		
		if instruction['instr'] == 'inc':
			self.__mem.setValue(instruction['reg'], self.__mem.getValue(instruction['reg']) + 1)
			return
			
		if instruction['instr'] == 'dec':
			self.__mem.setValue(instruction['reg'], self.__mem.getValue(instruction['reg']) - 1)
			return
			
		if instruction['instr'] == 'jnz':
			if 'val' in instruction:
				if int(instruction['val']) != 0:
					self.__curr += int(instruction['pos']) - 1
			else:
				if self.__mem.getValue(instruction['reg']) != 0:
					self.__curr += int(instruction['pos']) - 1
			return
			
	def __parse(self, line):
		for reg in self.__instructions:
			match = reg.match(line)
			if match is not None:
				return match.groupdict()
		raise ValueError('Bad line.')
		
def first(code):
	mem = Memory(['a', 'b', 'c', 'd'])
	p = Program(mem, code)
	
	p.run()
	
	print('\nFirst part:')
	print('\tData in register "a": ' + str(mem.getValue('a')))
	
	return mem.getValue('a')

def second(code):
	mem = Memory(['a', 'b', 'c', 'd'])
	p = Program(mem, 'cpy 1 c\r\n' + code)
	
	p.run()
	
	print('\nSecond part:')
	print('\tData in register "a": ' + str(mem.getValue('a')))
	
	return mem.getValue('a')

if __name__ == '__main__':
	code = open('input.txt').read()
	first(code)
	second(code)
