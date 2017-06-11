# Program execution file

# Import Quantum Gates
import QuantumGates

# Read Program File
file = open('Program.txt', 'r')

# Make it an Array
program = file.readlines()

# Initalize QBit array
QBits = [0] * (2**int(program[0]))
print len(QBits)

for i in xrange(1, len(program)): # loop all rows in 'Program.txt'
  command = program[i].split() # split row into array at spaces
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
  	
    
# Print Output After Circuit
print QBits

# Test
'''
print QuantumGates.Hadamard(0)
print QuantumGates.Hadamard(0)
'''