# Import Random Gates
import RandomGates

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
    #print 'NOT'
    #print command
    QBits[int(command[1])-1] = RandomGates.NOT(QBits[int(command[1])-1])
    #print QBits
    
  elif command[0] == 'CNOT':
    #print 'CNOT'
    #print command
    QBits[int(command[2])-1] = RandomGates.CNOT(QBits[int(command[1])-1], QBits[int(command[2])-1])
    #print QBits
    
  elif command[0] == 'CCNOT':
    #print 'CCNOT'
    #print command
    QBits[int(command[3])-1] = RandomGates.CCNOT(QBits[int(command[1])-1], QBits[int(command[2])-1], QBits[int(command[3])-1])
    #print QBits
    
  elif command[0] == 'COIN':
    #print 'COIN'
    #print command
    QBits[int(command[1])-1] = RandomGates.COIN()
    #print QBits
      
  elif command[0] == 'CCOIN':
    #print 'CCOIN'
    #print command
    QBits[int(command[1])-1] = RandomGates.CCOIN(QBits[int(command[1])-1])
    #print QBits
    
# Print Output After Circuit
print QBits

# Test
'''
print RandomGates.COIN()
print RandomGates.CCOIN(0)
print RandomGates.CCOIN(1)
'''