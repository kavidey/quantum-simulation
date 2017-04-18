def flipBit(num, bit):
	mask = 1 << (bit)	
	return num ^ mask

def swap(prob, bit, loc):	
	tmp = prob[loc]
	invert = flipBit(loc, bit)
	prob[loc] = prob[invert]
	prob[invert] = tmp
	return prob
	
def NOT(prob, qi):
	for i in xrange(0, len(prob)):
		mask = 1 << (qi)
		print bin(i & mask)
		if i & mask == 0:
			tmp = prob[i]
			invert = flipBit(i, qi)
			#print bin(invert)
			prob[i] = prob[invert]
			prob[invert] = tmp
	return prob

def CNOT(prob, qi, qj):
	for i in xrange(0, len(prob)):
		if flipBit(i, qi) == 0:
			prob = NOT(prob, qj)
	return prob

def CCNOT(prob, qi, qj, qk):
	for i in xrange(0, len(prob)):
		if flipBit(i, qi) == 0 and flipBit(i, qj) == 0:
			prob = NOT(prob, qk)
	return prob

		
Qubits = [1, 0, 0, 0]
print NOT(Qubits, 1)



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