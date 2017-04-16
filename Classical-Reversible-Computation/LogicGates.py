# Library to Store Logic Gates

# Logical NOT Function
def NOT(q):
  # Get and Return the NOT of q
  if q == 0:
    return 1  
  else:
    return 0
    
    
# Logical CNOT Function
def CNOT(q, qx):
  if q == 1:
    return NOT(qx)
    
  else:
    return qx
    
# Logical CCNOT Function
def CCNOT(q, qx, qy):
  if q == 1 and qx == 1:
    return NOT(qy)
    
  else:
    return qy
    