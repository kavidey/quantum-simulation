# Program execution file

# Import Quantum Gates
import QuantumGates

# Import Random
import random

# Read Program File
file = open('Program.txt', 'r')

# Make it an Array
program = file.readlines()

# Initalize QBit array and data storage array
QBits = [0] * (2**int(program[0]))
Data = [0] * (2**int(program[0]))

# Set first item to 1
QBits[0] = 1

# Set the deafault output as an array of probabilities
outputData = False

# Set the deafault number of times to loop when outputting actual data
times = 0

checkFirst = True

for i in xrange(1, len(program)): # loop all rows in 'Program.txt'
  command = program[i].split() # split row into array at spaces
  
  if i == 1:
  	try: # try
  		int(command[0]) # check if turning command[0] into an int returns an error
  		outputData =  True # change ouptutData to True (output result of running simulation)
  		times = int(command[0]) # set times to the value of command[0]
  	except ValueError: # except
  		outputData =  False # keep output data as false
       
  if command[0] == '#': # check if row is comment
    print 'comment: ' + str(program[i]) # if so print the comment
    
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
  	
  elif command[0] == 'Oracle': # check if row is a Oracle gate
  	QBits = QuantumGates.Oracle(QBits) # if so apply the Oracle gate
  
  elif command[0] == 'GroverDiffusion' or command[0] == 'GD': # check if row is Grover Diffusion
  	QBits = QuantumGates.GroverDiffusion(QBits) # if so apply the Grover Diffusion
  	checkFirst = False

if outputData == False:
	print QBits
else:
	for i in range(0, times):
		test = random.uniform(0.0,1.0)
		if checkFirst == True:
			prob = QBits[0]**2
			for i in range(0, len(QBits)):
				if test < prob and test > (prob - (QBits[i]**2)):
					Data[i] = Data[i]+1
				if i != len(QBits)-1:
					prob = prob + (QBits[i+1]**2)
				if QBits[i] == 0:
					Data[i] = 0
		else:	
			prob = QBits[1]**2
			for i in range(1, len(QBits)):
				if test < prob and test > (prob - (QBits[i]**2)):
					Data[i] = Data[i]+1
				if i != len(QBits)-1:
					prob = prob + (QBits[i+1]**2)
				if QBits[i] == 0:
					Data[i] = 0
	print Data
