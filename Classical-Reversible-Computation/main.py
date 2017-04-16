# Import Logic Gates
import LogicGates

# Initalize QBit array
QBits = [0,0,0,0,0]

# Read Program File
file = open('Program.txt', 'r')

# Make it an Array
program = file.readlines()

for i in xrange(0, len(program)):
  command = program[i].split()
  if command[0] == '#':
    print 'comment'
    print command
  elif command[0] == 'NOT':
    print 'NOT'
    #print command
    QBits[int(command[1])-1] = LogicGates.NOT(QBits[int(command[1])-1])
    print QBits
    
  elif command[0] == 'CNOT':
    print 'CNOT'
    #print command
    QBits[int(command[2])-1] = LogicGates.CNOT(QBits[int(command[1])-1], QBits[int(command[2])-1])
    print QBits
    
  elif command[0] == 'CCNOT':
    print 'CCNOT'
    #print command
    QBits[int(command[3])-1] = LogicGates.CCNOT(QBits[int(command[1])-1], QBits[int(command[2])-1], QBits[int(command[3])-1])
    print QBits
    
# Test
'''
print LogicGates.NOT(1)
print LogicGates.CNOT(1, 1)
print LogicGates.CCNOT(0, 1, 0)
'''