# Quantum Gates Library

# Import necessary libraries
import math
import cmath

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
	tmp = amp[loc] # store amp[loc] in tmp
	invert = flipBit(loc, bit) # find the inverted location
	amp[loc] = amp[invert] # set amp[invert] to amp[loc] 
	amp[invert] = tmp # set amp[invert] to tmp (the old amp[loc])
	return amp

# Function used in Grovers Algorithm 
def F(qi):
	# qi -- value to check
	if qi == 2: # check if qi is 2
		return 1 # if so return 1
	return 0 # otherwise return 0
	
# Function that rounds all items in an array 
# to the nearist simple decimial
def round(amp):
	# amp -- array to be rounded
	for i in range(0, len(amp)): # loop through all items in array
		if amp[i] < 0.000001 and amp[i] > -0.000001: # check if item is between 0.000001 and -0.000001
			amp[i] = 0 # if so set item to 0
		elif amp[i] < 1.000001 and amp[i] > 0.999999: # check if item is between 1.000001 and 0.999999
			amp[i] = 1 # if so set item to 1
		elif amp[i] < 0.5 and amp[i] > 0.499999: # check if item is between 0.5 and 0.499999
			amp[i] = 0.5 # if so set item to 0.5
	return amp # return the new array
	
# NOT gate (flips the amplitudes of all pairs)
def NOT(amp, qi):
	# amp -- array of data
	# qi -- qubit to be NOT'd
	# maski -- binary mask used to only apply NOT's when the control bit is 0
	maski = 1 << qi
	for i in xrange(0, len(amp)): # loop through all inputs
		if i & maski == 0: # check whether bit qi in i is 0
			amp = swap(amp, i, qi) # swap items in amp
	return amp # return the new array

# CNOT gate (flips the amplitude of a pair if a selected bit is 1)
def CNOT(amp, qi, qj):
	# amp -- array of data
	# qi -- controller bit
	# qj -- qubit to be NOT'd
	# maski -- binary mask used to only apply CNOT's when the control bit is 1
	maski = 1 << qi
	for i in xrange(0, len(amp)): # loop through all inputs
		if i & maski != 0: # check if control bit (qi) is one
			amp = swap(amp, i, qj) # if so swap that bit and its inverse
	return amp # return the new array

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
	for i in xrange(0, len(amp)): # loop through all inputs
		if i & maski != 0 and i & maskj != 0: # check if control bits qi and qj are one
			if i & maskj == 0: # check whether bit qi in i is 0
				amp = swap(amp, i, qk) # if so swap that bit and its inverse
	return amp # return the new array
	
# Hadamard gate (like a COIN gate but with negative amplitudes)
def Hadamard(amp, qi):
	# amp -- array of data
	# maski -- binary mask used to only apply Hadamards's when the control bit is 0
	# sqrtTwo -- variable to store the square root of 2
	# qi -- qbit to apply the Hadamard gate to
	sqrtTwo = 1.4142135623730951
	maski = 1 << qi
	for i in range(0, len(amp)): # loop through all inputs
		if i & maski == 0: # check if control bit is 0
			flip = flipBit(i, qi) # get the flipped location
			a = amp[i] # store amp[i] in a
			b = amp[flip] # store amp[flip] in b
			amp[i] = (1/sqrtTwo) * (a+b) # set amp[i] to 1/sqrt2 * (a+b)
			amp[flip] = (1/sqrtTwo) * (a-b )# set amp[flip] to 1/sqrt2 * (a-b)
	#return round(amp)
	return amp 
	
# Z-NOT gate (inverts the the amplitude of all qbits except the first one)  
def ZNOT(amp):
	# amp -- array of data
	for i in range(1, len(amp)): # loop through all inputs
		amp[i] = amp[i]*-1 # invert
	return amp
	
# Oracle gate (used in grovers algorithm)
def Oracle(amp):
	# amp -- array of data
	for i in range(0, len(amp)): # loop through all inputs
		if F(i) == 1: # if F(i) is 1
			amp[i] = amp[i] * -1 # multiply the amplitude by -1
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
def Omega(qi, qj, pwr, amp):
	# amp -- array of data
	# qi -- controller bit
	# qj -- qubit to be NOT'd
	# maski -- binary mask used to only apply CNOT's when the control bit is 1
	# pwr -- number used as exponent
	maski = 1 << qi
	if i & maski != 0: # check if control bit (qi) is one
		comp = cmath.polar(amp[qj]) # store amp{qj] in comp
		num = float(len(amp)) # store the length of amp in num
		shift = pwr/num # store the amount to turn by in shift 
		comp = cmath.polar(complex(comp[0], comp[1] + shift)) # shift comp
		amp[qj] = cmath.rect(comp) # store comp in amp[qj]
	return amp # output amp
	
# Hadamard Gate over Z to the n
def HZn(amp):
	num = math.log(len(amp), 2)
	num = int(num)
	for i in range(num, 1, -1):
		Hadamard(amp, i-1)
		check = 1
		for j in range(num, num-i):
			if j > 1:
				Omega(check, i, -((j-2)**2), amp)
				check = check + 1
	Hadamard(amp, 0)
	return amp