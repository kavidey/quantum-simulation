# Quantum Gates Library

# Function to flip a bit
def flipBit(num, bit):
	# num -- the number whose bit gets flipped
	# bit -- the bit that gets flipped
	mask = 1 << (bit)	# generate a mask for bit
	return num ^ mask # XOR the mask and num

# Flip 2 items in an array,
# 1st specified by loc
# 2nd by flipBit(loc, bit)
def swap(prob, loc, bit):
	# prob -- array of data
	# loc -- index of 1st item
	# bit -- used to calculate index of 2nd item
	tmp = prob[loc] # store prob[loc] in tmp
	invert = flipBit(loc, bit) # find the inverted location
	prob[loc] = prob[invert] # set prob[invert] to prob[loc] 
	prob[invert] = tmp # set prob[invert] to tmp (the old prob[loc])
	return prob
	
# Function that rounds all items in an array 
# to the nearist simple decimia
def round(prob):
	# prob -- array to be rounded
	for i in range(0, len(prob)): # loop through all items in array
		if prob[i] < 0.000001 and prob[i] > -0.000001: # check if item is between 0.000001 and -0.000001
			prob[i] = 0 # if so set item to 0
		elif prob[i] < 1.000001 and prob[i] > 0.999999: # check if item is between 1.000001 and 0.999999
			prob[i] = 1 # if so set item to 1
		elif prob[i] < 0.5 and prob[i] > 0.499999: # check if item is between 0.5 and 0.499999
			prob[i] = 0.5 # if so set item to 0.5
	return prob # return the new array
	
# NOT gate (flips the probabilities of all pairs)
def NOT(prob, qi):
	# prob -- array of data
	# qi -- qubit to be NOT'd
	# maski -- binary mask used to only apply NOT's when the control bit is 0
	maski = 1 << qi
	for i in xrange(0, len(prob)): # loop through all inputs
		if i & maski == 0: # check whether bit qi in i is 0
			prob = swap(prob, i, qi) # swap items in prob
	return prob # return the new array

# CNOT gate (flips the probabilities of a pair if a selected bit is 1)
def CNOT(prob, qi, qj):
	# prob -- array of data
	# qi -- controller bit
	# qj -- qubit to be NOT'd
	# maski -- binary mask used to only apply CNOT's when the control bit is 1
	maski = 1 << qi
	for i in xrange(0, len(prob)): # loop through all inputs
		if i & maski != 0: # check if control bit (qi) is one
			prob = swap(prob, i, qj) # if so swap that bit and its inverse
	return prob # return the new array

# CCNOT gate (flips the probabilities of a pair if the selected bits are both 1)
def CCNOT(prob, qi, qj, qk):
	# prob -- array of data
	# qi -- 1st controller bit
	# qj -- 2nd controller bit
	# qk -- qubit to be NOT'd
	# maski -- binary mask used to only apply CCNOT's when the control bits are 1
	# maskj -- binary mask used to only apply CCNOT's when the control bits are 1
	maski = 1 << qi
	maskj = 1 << qj
	for i in xrange(0, len(prob)): # loop through all inputs
		if i & maski != 0 and i & maskj != 0: # check if control bits qi and qj are one
			if i & maskj == 0: # check whether bit qi in i is 0
				prob = swap(prob, i, qk) # if so swap that bit and its inverse
	return prob# return the new array
	
# Hadamard gate (like a COIN gate but with negative amplitudes)
def Hadamard(prob, qi):
	# prob -- array of data
	# maski -- binary mask used to only apply Hadamards's when the control bit is 0
	# sqrtTwo -- variable to store the square root of 2
	# qi -- qbit to apply the Hadamard gate to
	sqrtTwo = 1.4142135623730951
	maski = 1 << qi
	for i in range(0, len(prob)): # loop through all inputs
		if i & maski == 0: # check if control bit is 0
			flip = flipBit(i, qi) # get the flipped location
			a = prob[i] # store prob[i] in a
			b = prob[flip] # store prob[flip] in b
			prob[i] = (1/sqrtTwo) * (a+b) # set prob[i] to 1/sqrt2 * (a+b)
			prob[flip] = (1/sqrtTwo) * (a-b )# set prob[flip] to 1/sqrt2 * (a-b)
	return round(prob) 