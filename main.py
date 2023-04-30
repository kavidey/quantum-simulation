import random
import cmath

import QuantumGates

def Run():
	# Read Program File
	file = open('Program.txt', 'r')

	# Make it an Array
	program = file.readlines()

	# Initalize QBit array and data storage array
	QBits = [complex(0.0, 0.0)] * (2**int(program[0]))
	Data = [0] * (2**int(program[0]))

	# Set first item to 1
	QBits[0] = complex(1.0 ,0.0)

	# Set the default output as an array of probabilities
	outputData = False

	# Set the deafault number of times to loop when outputting actual data
	times = 0

	checkFirst = True
	for i in range(1, len(program)): # loop all rows in 'Program.txt'
		command = program[i].strip().split() # split row into array at spaces
		if command:
			if i == 1:
				try: # try
					int(command[0]) # check if turning command[0] into an int returns an error
					outputData =  True # change ouptutData to True (output result of running simulation)
					times = int(command[0]) # set times to the value of command[0]
				except ValueError: # except
					outputData =  False # keep output data as false
		
			if command[0] == '#': # check if row is comment
				print(str(program[i]))#[:-2] # if so print the comment
		
			elif command[0] == 'NOT': # check if row is a NOT gate
				QBits = QuantumGates.NOT(QBits,int(command[1])) # if so apply the NOT gate
		
			elif command[0] == 'CNOT': # check if row is a CNOT gate
				QBits = QuantumGates.CNOT(QBits, int(command[1]), int(command[2])) # if so apply the CNOT gate
		
			elif command[0] == 'CCNOT': # check if row is a CCNOT gate
				QBits = QuantumGates.CCNOT(QBits, int(command[1]), int(command[2]), int(command[3])) # if so apply the CCNOT gate
		
			elif command[0] == 'H' or command[0] == 'Hadamard': # check if row is a Hadamard gate
				QBits = QuantumGates.Hadamard(QBits, int(command[1])) # if so apply the Hadamard gate
		
			elif command[0] == 'ZNOT': # check if row is a ZNOT gate
				QBits = QuantumGates.ZNOT(QBits) # if so apply the ZNOT gate
		
			elif command[0] == 'OracleGA': # check if row is a Oracle gate (oracle from Grovers Algorithm)
				QBits = QuantumGates.OracleGA(QBits) # if so apply the Oracle gate (oracle from Grovers Algorithm)
	
			elif command[0] == 'GroverDiffusion' or command[0] == 'GD': # check if row is Grover Diffusion
				QBits = QuantumGates.GroverDiffusion(QBits) # if so apply the Grover Diffusion
				checkFirst = False
		
			elif command[0] == 'HadamardOverZn' or command[0] == 'HZn': # check if row is Hadamard over Z to the n
				QBits = QuantumGates.HZn(QBits, int(command[1])) # if so apply Hadamard over Z to the n
		
			elif command[0] == 'ADD': # check if row is add
				QBits = QBits + ([complex(0, 0)] * ( ( 2**(int(command[1]) + int(program[0]) ) ) - len(QBits) ) ) # if so add n QBits to QBits
				Data = Data + ([0] * ( ( 2**(int(command[1]) + int(program[0]) ) ) - len(Data) ) ) # and Data
			
			elif command[0] == 'OracleSA': # check if row is a Oracle gate (oracle from Shor's Algorithm)
				QBits = QuantumGates.OracleSA(QBits, int(program[0])) # if so apply the Oracle gate (oracle from Shor's Algorithm)
		
			elif command[0] == 'Measure' or command[0] == 'M': # check if row is Measure
				QBits = QuantumGates.Measure(QBits, int(command[1]), times) # if so measure
					
			elif command[0] == 'R': # check if row is Rotate
				array = program[i][2:]
				array = array.split(',')
				array = [float(i) for i in array]
				QBits = QuantumGates.Rotate(QBits, array) # if so rotate


	if outputData == False:
		squared = []
		for i in range(0, len(QBits)):
			squared.append((cmath.polar(QBits[i])[0])**2)
		return squared
	else:
		for i in range(0, times):
			test = random.uniform(0.0,1.0)
			if checkFirst == True:
				prob = (cmath.polar(QBits[0])[0])**2
				for i in range(0, len(QBits)):
					if test < prob and test > (prob - (cmath.polar(QBits[i])[0])**2):
						Data[i] = Data[i]+1
					if i != len(QBits)-1:
						prob = prob + (cmath.polar(QBits[i])[0])**2
					if QBits[i] == 0:
						Data[i] = 0
			else:	
				prob = (cmath.polar(QBits[1]).r)**2
				for i in range(1, len(QBits)):
					if test < prob and test > (prob - (cmath.polar(QBits[i])[0])**2):
						Data[i] = Data[i]+1
					if i < len(QBits)-1:
						prob = prob + (cmath.polar(QBits[i])[0])**2
					if QBits[i] == 0:
						Data[i] = 0
		return Data

if __name__ == "__main__":
	print(Run())
