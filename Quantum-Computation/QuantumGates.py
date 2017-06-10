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
	tmp = prob[loc]
	invert = flipBit(loc, bit)
	prob[loc] = prob[invert]
	prob[invert] = tmp
	return prob
	
def round(prob):
	for i in range(0, len(prob)):
		if prob[i] < 0.000000001 and prob[i] > -0.000000001:
			prob[i] = 0
		elif prob[i] < 1.00000001 and prob[i] > 0.99999999:
			prob[i] = 1
	return prob
	
# NOT gate (flips the probabilities of all pairs)
def NOT(prob, qi):
	# prob -- array of data
	# qi -- qubit to be NOT'd
	mask = 1 << qi
	for i in xrange(0, len(prob)): # Loop through all outputs
		if i & mask == 0: # check whether bit qi in i is 0
			prob = swap(prob, i, qi) # swap items in prob
	return prob

# CNOT gate (flips the probabilities of a pair if a selected bit is 1)
def CNOT(prob, qi, qj):
	# prob -- array of data
	# qi -- controller bit
	# qj -- qubit to be NOT'd
	maski = 1 << qi
	for i in xrange(0, len(prob)):
		if i & maski != 0:
			prob = swap(prob, i, qj)
	return prob

# CCNOT gate (flips the probabilities of a pair if the selected bits are both 1)
def CCNOT(prob, qi, qj, qk):
	# prob -- array of data
	# qi -- 1st controller bit
	# qj -- 2nd controller bit
	# qk -- qubit to be NOT'd
	maski = 1 << qi
	maskj = 1 << qj
	for i in xrange(0, len(prob)):
		if i & maski != 0 and i & maskj != 0:
			if i ^ maskj == 1:
				prob = swap(prob, i, qk)
	return prob
	
	
def Hadamard(prob, qi):
	sqrtTwo = 1.4142135623730951
	maski = 1 << qi
	for i in range(0, len(prob)):
		if i & maski != 1:
			print i
			flip = flipBit(i, qi)
			print flip
			if prob[i] == 1 or prob[i] == 0:
				if prob[i] != 0:
					if maski & i == 0:
						prob[i] = (1/sqrtTwo)*(prob[i])
					else:
						prob[i] = (-(1/sqrtTwo))*(prob[i])
					if prob[flip] == 0:
						prob[flip] = 1
					if maski & flip == 0:
						prob[flip] = (1/sqrtTwo)*(prob[flip])
					else:
						prob[flip] = (-(1/sqrtTwo))*(prob[flip])
			
			else:
				if prob[i] != 0:
					if maski & i == 0:
						prob[i] = (1/sqrtTwo)*((prob[i])*2)
						print 'i pos'
					else:
						prob[i] = (1/sqrtTwo)*(prob[i]+prob[flip])
						print 'i neg'
					if maski & flip == 0:
						prob[flip] = (1/sqrtTwo)*(prob[flip]*2)
						print 'fl pos'
					else:
						prob[flip] = ((1/sqrtTwo)*prob[i])+prob[flip]	
						print 'fl neg'
						
		return round(prob)
		
Qubits = [1, 0, 0, 0]
print Hadamard(Qubits, 0)
print CNOT(Qubits, 0, 1)
print Hadamard(Qubits, 0)


# Old Code
'''
def opposite(num):
  if num == 0:
    return 1  
  else:
    return 0
    	
def flipBit(num, bit):
	binNum = ''.join(reversed(bin(num).lstrip('0b')))
	for i in xrange(0, 6):
		while len(binNum) < 5:
			binNum = binNum + '0'
	#print binNum
	#print bit - 1
		flip = opposite(int(binNum[bit-1]))
	binStr = ''.join(reversed(binNum[:bit-1] + str(flip) + binNum[bit-1]))
	return int('0b' + binStr, 2)		
'''