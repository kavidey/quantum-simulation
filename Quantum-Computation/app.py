import main
import math
import random
from numpy import kron

program = open('Program.txt', 'w')
program.truncate()
program.write('2')
program.write('\n')

x = random.randint(0, 1)
y = random.randint(0, 1)
x = 1
y = 1

if x == 0 and y == 0:
	#rotation = [0,math.pi/8]
	rotation = '0,'+str(math.pi/8)
	
if x == 0 and y == 1:
	#rotation = [0,-(math.pi/8)]
	rotation = '0,'+str(-(math.pi/8))
	
if x == 1 and y == 0:
	#rotation = [math.pi/4,math.pi/8]
	rotation = str(math.pi/4)+','+str(math.pi/8)
	
if x == 1 and y == 1:
	#rotation = [math.pi/4,-(math.pi/8)]
	rotation = str(math.pi/4)+','+str(-(math.pi/8))
	
	
program.write('R ' + rotation)
program.write('\n')
program.write('M 0')
program.write('\n')
program.write('M 1')
program.write('\n')
program.close()

output = main.Run()
state = 0
a = 0
b = 0
for i in range(0, len(output)):
	if output[i] >= 1:
		state = i
if state == 0:
	a = 0
	b = 0
elif state == 1:
	a = 1
	b = 0
elif state == 2:
	a = 0
	b = 1
elif state == 3:
	a = 1
	b = 1
print 'Ref 1: '+str(x)
print 'Ref 2: '+str(y)
print 'Player A: '+str(a)
print 'Player B: '+str(b)
print 'Ref\'s bits XOR\'ed: ' + str(x^y)
print 'Kronecker product of Players bits: ' + str(kron(a, b))
if x^y == kron(a, b):
	print 'Players Win!!!!!!!'
else:
	print 'players loose :('