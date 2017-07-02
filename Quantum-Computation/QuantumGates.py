# Quantum Gates Library

# Import necessary libraries
import math
import cmath
import random

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
def FGA(qi):
	# qi -- value to check
	if qi == 2: # check if qi is 2
		return 1 # if so return 1
	return 0 # otherwise return 0
	
# Function to find the period of with Shor's Algorithm 	
def FSA(qi):
	# qi -- input to function
	return qi % 4 # return qi mod 4
	
# Function that rounds all items in an array 
# to the nearist simple decimial
def Round(amp):
	# amp -- array to be rounded
	for i in range(0, len(amp)): # loop through all items in array
		if cmath.polar(amp[i])[0] < 0.000001 and cmath.polar(amp[i])[0] > -0.000001: # check if item is between 0.000001 and -0.000001
			amp[i] = complex(0, 0) # if so set item to 0
		elif cmath.polar(amp[i])[0] < 1.000001 and cmath.polar(amp[i])[0] > 0.999999: # check if item is between 1.000001 and 0.999999
			amp[i] = cmath.rect(1, cmath.polar(amp[i])[1]) # if so set item to 1
		elif cmath.polar(amp[i])[0] < 0.5 and cmath.polar(amp[i])[0] > 0.499999: # check if item is between 0.5 and 0.499999
			amp[i] = cmath.rect(0.5, cmath.polar(amp[i])[1]) # if so set item to 0.5
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
			amp[flip] = (1/sqrtTwo) * (a-b)# set amp[flip] to 1/sqrt2 * (a-b)
	return amp
	
# Z-NOT gate (inverts the the amplitude of all qbits except the first one)  
def ZNOT(amp):
	# amp -- array of data
	for i in range(1, len(amp)): # loop through all inputs
		amp[i] = amp[i]*-1 # invert
	return amp
	
# Oracle gate (used in grovers algorithm)
def OracleGA(amp):
	# amp -- array of data
	for i in range(0, len(amp)): # loop through all inputs
		if FGA(i) == 1: # if FGA(i) is 1
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
def Omega(qi, qj, pwr, amp, num):
	# amp -- array of data
	# qi -- controller bit
	# qj -- qubit to be shifted
	# maski -- binary mask used to only apply shifts when the control bit is 1
	# pwr -- number used as exponent
	maski = 1 << qi
	maskj = 1 << qj
	print "qi = %d, qj = %d, pwr = %d" % (qi, qj, pwr)
	for i in range(0, len(amp)):
		if i & maski != 0 and i & maskj != 0: # check if control bit (qi) is one
			comp = cmath.polar(amp[i]) # store amp[qj] in comp
			num = float(2 ** num) # store the length of amp in num
			shift = pwr/num # store the amount to turn by in shift 
			print i, shift
			shift *= cmath.pi * 2
			amp[i] = cmath.rect(comp[0], comp[1] + shift) # store comp in amp[qj]
	return amp # output amp
	
# Hadamard Gate over Z to the n
def HZn(amp, num):
	# amp -- array of data
	# num -- number of QBits of apply over
	for i in range(num, 0, -1): # loop backwards from num to 0
		Hadamard(amp, i-1) # apply a Hadamard Gate to the QBit i-1
		check = 1 # set check to 1
		for j in range(num, num-(i-1), -1): # loop backwards from num to num-(i-1)
			amp = Omega(i-check-1, i-1, -(2**(j-2)), amp, num) # apply an Omega gate on QBit i with i-check-1 as the controller bit and -(2**(j-2)) as the exponent
			check = check + 1 # increase check by 1
	return amp
	
# Oracle gate (used in Shor's algorithm)
def OracleSA(amp, n):
	for i in range(0, 2**n): # loop from 0 to 2 to the n
		output = FSA(i) << n # set output to the result of FSA(i) shifted n bits to the right
		tmp = amp[i] # store amp[i] in tmp
		amp[i] = amp[output+i] # set amp[i+output] to amp[i] 
		amp[output+i] = tmp # set amp[i+output] to tmp (the old amp[i])
	return amp # return amp
	
# Measurement gate (used to measure a single QBit)
def Measure(amp, qi, times):
	# amp -- array of data
	# qi -- QBit to be measured
	# maski -- binary mask used to check if the control bit is 1
	maski = 1 << qi
	Zero = 0
	One = 0
	for i in range(0, len(amp)): # loop through all amplitudes
		if i & maski != 0: # check if amp[i] is 0
			One = One + cmath.polar(amp[i])[0]**2 # add amp[i] squared to One
		else: # otherwise
			Zero = Zero + cmath.polar(amp[i])[0]**2 # add amp[i] squared to Zero
	Data = [0,0] # create a variable to store data from random numbers
	test = random.uniform(0.0,1.0) # get a random number between 0 and 1
	if test < Zero: # check if test is less than 0
		state = 0 # set state to 0
	else: # otherwise
		state = 1 # set state to 1
	norm = 0 # set norm to 0
	if state == 1: # check if state is 1
		for i in range(0, len(amp)): # loop through amp
			if i & maski != 0: # check if qi is 1 in i
				norm = norm + (cmath.polar(amp[i])[0])**2 # add the length of amp[i] squared to norm
	if state == 0: # check if state is 0
		for i in range(0, len(amp)): # loop through amp
			if i & maski != 0: # check if qi is 1 in i
				pass # do nothing
			else: # otherwise
				norm = norm + (cmath.polar(amp[i])[0])**2 # add the length of amp[i] squared to norm
	norm = 1/norm # set norm to divied 1 by norm
	norm = math.sqrt(norm) # set norm to the square root of norm
	if state == 0: # if state is 0
		for i in range(0, len(amp)): # loop throught everything in amp
			if i & maski != 0: # check if qi is 1 in i
				amp[i] = complex(0.0, 0.0) # set amp[i] to complex 0
	if state == 1: # if state is 1
		for i in range(0, len(amp)): # loop throught everything in amp
			if i & maski != 0: # check if qi is 1 in i
				pass # do nothing
			else: # otherwise
				amp[i] = complex(0.0, 0.0) # set amp[i] to complex 0
	for i in range(0, len(amp)): # loop throught everything in amp
		amp[i] = amp[i] * norm # set amp to amp times norm
	return amp # return amp

if __name__ == "__main__":
	amp = [complex(0.5, 0.0), complex(0.0, 0.0)] * 4
	print HZn(amp, 3)