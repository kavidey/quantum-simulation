# Quantum Gates Library
import math
import cmath
import random
import numpy as np

# Function to flip a bit
def flipBit(num, bit):
	# num -- the number whose bit gets flipped
	# bit -- the bit that gets flipped
	mask = 1 << (bit)	# generate a mask for bit
	return num ^ mask # XOR the mask and num

# Flip 2 items in an array,
# 1st specified by loc
# 2nd by flipBit(loc, bit)
def swap(amp, loc, bit):
	# amp -- array of data
	# loc -- index of 1st item
	# bit -- used to calculate index of 2nd item
	tmp = amp[loc]
	invert = flipBit(loc, bit) # find the inverted location
	if invert > loc:
		amp[loc] = amp[invert]
		amp[invert] = tmp
	return amp

# Function used in Grovers Algorithm 
def FGA(qi):
	# qi -- value to check
	if qi == 2:
		return 1
	return 0
	
# Find the period of with Shor's Algorithm 	
def FSA(qi):
	# qi -- input to function
	return qi % 4 # return qi mod 4
	
# Round all items in an array to the nearest simple decimal
def Round(amp):
	# amp -- array to be rounded
	for i in range(0, len(amp)):
		if cmath.polar(amp[i])[0] < 0.000001 and cmath.polar(amp[i])[0] > -0.000001:
			amp[i] = complex(0, 0)
		elif cmath.polar(amp[i])[0] < 1.000001 and cmath.polar(amp[i])[0] > 0.999999:
			amp[i] = cmath.rect(1, cmath.polar(amp[i])[1])
		elif cmath.polar(amp[i])[0] < 0.5 and cmath.polar(amp[i])[0] > 0.499999:
			amp[i] = cmath.rect(0.5, cmath.polar(amp[i])[1])
	return amp
	
# NOT gate (flips the amplitudes of all pairs)
def NOT(amp, qi):
	# amp -- array of data
	# qi -- qubit to be NOT'd
	# maski -- binary mask used to only apply NOT's when the control bit is 0
	maski = 1 << qi
	for i in xrange(0, len(amp)):
		if i & maski == 0: # check whether bit qi in i is 0
			amp = swap(amp, i, qi) # swap items in amp
	return amp

# CNOT gate (flips the amplitude of a pair if a selected bit is 1)
def CNOT(amp, qi, qj):
	# amp -- array of data
	# qi -- controller bit
	# qj -- qubit to be NOT'd
	# maski -- binary mask used to only apply CNOT's when the control bit is 1
	maski = 1 << qi
	for i in range(0, len(amp)):
		if i & maski != 0: # check if control bit (qi) is one
			amp = swap(amp, i, qj) # if so swap that bit and its inverse
	return amp

# CCNOT gate (flips the amplitude of a pair if the selected bits are both 1)
def CCNOT(amp, qi, qj, qk):
	# amp -- array of data
	# qi -- 1st controller bit
	# qj -- 2nd controller bit
	# qk -- qubit to be NOT'd
	# maski -- binary mask used to only apply CCNOT's when the control bits are 1
	# maskj -- binary mask used to only apply CCNOT's when the control bits are 1
	maski = 1 << qi
	maskj = 1 << qj
	for i in range(0, len(amp)):
		if i & maski != 0 and i & maskj != 0: # check if control bits qi and qj are one
			if i & maskj == 0: # check whether bit qi in i is 0
				amp = swap(amp, i, qk) # if so swap that bit and its inverse
	return amp
	
# Hadamard gate (like a COIN gate but with negative amplitudes)
def Hadamard(amp, qi):
	# amp -- array of data
	# maski -- binary mask used to only apply Hadamards's when the control bit is 0
	# sqrtTwo -- variable to store the square root of 2
	# qi -- qbit to apply the Hadamard gate to
	sqrtTwo = 1.4142135623730951
	maski = 1 << qi
	for i in range(0, len(amp)):
		if i & maski == 0:
			flip = flipBit(i, qi)
			a = amp[i]
			b = amp[flip]
			amp[i] = (1/sqrtTwo) * (a+b)
			amp[flip] = (1/sqrtTwo) * (a-b)
	return amp
	
# Z-NOT gate (inverts the the amplitude of all qbits except the first one)  
def ZNOT(amp):
	# amp -- array of data
	for i in range(1, len(amp)):
		amp[i] = amp[i]*-1 # invert
	return amp
	
# Oracle gate (used in grovers algorithm)
def OracleGA(amp):
	# amp -- array of data
	for i in range(0, len(amp)): # loop through all inputs
		if FGA(i) == 1:
			amp[i] = amp[i] * -1
	return amp
	
# Grover Diffusion
def GroverDiffusion(amp):
	# amp -- array of data
	for i in range(0, int(math.log(len(amp), 2))): # loop through all qbits
		Hadamard(amp, i) # apply a hadamard gat
	ZNOT(amp) # apply a ZNOT gate
	for i in range(0, int(math.log(len(amp), 2))): # loop through all qbits
		Hadamard(amp, i)
	return amp # apply a ZNOT gate
	
# Omega gate (phase shift gate)
def Omega(qi, qj, pwr, amp, num):
	# amp -- array of data
	# qi -- controller bit
	# qj -- qubit to be shifted
	# maski -- binary mask used to only apply shifts when the control bit is 1
	# pwr -- number used as exponent
	maski = 1 << qi
	maskj = 1 << qj
	N = float(2 ** num) # store the length of amp in num
	#print("qi = %d, qj = %d, pwr = %d" % (qi, qj, pwr))
	for i in range(0, len(amp)):
		if i & maski != 0 and i & maskj != 0: # check if control bit (qi) is one
			comp = cmath.polar(amp[i])
			shift = pwr/N # store the amount to turn by in shift 
			shift *= cmath.pi * 2
			amp[i] = cmath.rect(comp[0], comp[1] + shift)
	return amp # output amp
	
# Hadamard Gate over Z to the n
def HZn(amp, num):
	# amp -- array of data
	# num -- number of QBits of apply over
	for i in range(num, 0, -1):
		Hadamard(amp, i-1)
		check = 1
		for j in range(num, num-(i-1), -1):
			amp = Omega(i-check-1, i-1, -(2**(j-2)), amp, num) # apply an Omega gate on QBit i with i-check-1 as the controller bit and -(2**(j-2)) as the exponent
			check = check + 1
	return amp
	
# Oracle gate (used in Shor's algorithm)
def OracleSA(amp, n):
	for i in range(0, 2**n):
		output = FSA(i) << n
		tmp = amp[i]
		amp[i] = amp[output+i]
		amp[output+i] = tmp
	return amp
	
# Measurement gate (used to measure a single QBit)
def Measure(amp, qi, times):
	# amp -- array of data
	# qi -- QBit to be measured
	# maski -- binary mask used to check if the control bit is 1
	maski = 1 << qi
	Zero = 0
	One = 0
	for i in range(0, len(amp)):
		if i & maski != 0: # check if amp[i] is 0
			One = One + cmath.polar(amp[i])[0]**2 # add amp[i] squared to One
		else:
			Zero = Zero + cmath.polar(amp[i])[0]**2 # add amp[i] squared to Zero
	Data = [0,0]
	test = random.uniform(0.0,1.0)
	if test < Zero:
		state = 0
	else:
		state = 1
	norm = 0
	if state == 1:
		for i in range(0, len(amp)):
			if i & maski != 0: # check if qi is 1 in i
				norm = norm + (cmath.polar(amp[i])[0])**2 # add the length of amp[i] squared to norm
	if state == 0:
		for i in range(0, len(amp)):
			if i & maski != 0: # check if qi is 1 in i
				pass
			else:
				norm = norm + (cmath.polar(amp[i])[0])**2 # add the length of amp[i] squared to norm
	norm = 1/norm
	norm = math.sqrt(norm)
	if state == 0:
		for i in range(0, len(amp)):
			if i & maski != 0: # check if qi is 1 in i
				amp[i] = complex(0.0, 0.0)
	if state == 1:
		for i in range(0, len(amp)):
			if i & maski != 0: # check if qi is 1 in i
				pass
			else:
				amp[i] = complex(0.0, 0.0)
	for i in range(0, len(amp)):
		amp[i] = amp[i] * norm
	return amp
	
	
def Rotate(amp, rot):
	r = rot[0]
	matrix = np.array([[math.cos(r), math.sin(r)], [math.sin(r), -(math.cos(r))]])
	for i in range(1, len(rot)):
		r = rot[i]
		m = np.array([[math.cos(r), math.sin(r)], [math.sin(r), -(math.cos(r))]])
		matrix = np.kron(m, matrix)
	return np.inner(matrix, amp)

if __name__ == '__main__':
	print(CNOT([1/math.sqrt(2), 0, 1/math.sqrt(2), 0], 1, 0))
	#print Rotate([1/math.sqrt(2), 0, 1/math.sqrt(2), 0], [math.pi/4, 0])