import gf


# Affine transformation in Galois' field, with constant 0x1F
# This can be done in columns with least significant byte first.
# Resulting matrix is the same adding rows starting with
# right rotated bit.


def makematrix():
	matrixbits = [0,0,0,1,1,1,1,1] # 0x1F
	affmatrix = []
	for i in range(8):
		matrixbits = gf.circrotateright(matrixbits)
		affmatrix.append(matrixbits)

	return affmatrix


def makeinversematrix():
	matrixbits = [0,1,0,0,1,0,1,0] # inverse of 0x1F (in GF?)
	affmatrix = []
	for i in range(8):
		matrixbits = gf.circrotateright(matrixbits)
		affmatrix.append(matrixbits)

	return affmatrix


def transform(a, affmatrix):
	alsb = list(reversed(a))
	result = []

	for i in range(len(affmatrix)):

		tempbits = []
		for j in range(len(a)):
			tempbits.append(affmatrix[i][j] & alsb[j])

		result.append(tempbits[0])

		for k in range(1,8):
			result[i] = result[i] ^ tempbits[k]

	resultmsb = list(reversed(result))

	finalvector = [0,1,1,0,0,0,1,1] # 0x63
	finalvalue = []

	for i in range(len(resultmsb)):
		finalvalue.append(resultmsb[i] ^ finalvector[i])

	return finalvalue


def inversetransform(a, affmatrix):
	alsb = list(reversed(a))
	result = []

	for i in range(len(affmatrix)):

		tempbits = []
		for j in range(len(a)):
			tempbits.append(affmatrix[i][j] & alsb[j])

		result.append(tempbits[0])

		for k in range(1,8):
			result[i] = result[i] ^ tempbits[k]

	resultmsb = list(reversed(result))

	finalvector = [0,0,0,0,0,1,0,1]
	finalvalue = []

	for i in range(len(resultmsb)):
		finalvalue.append(resultmsb[i] ^ finalvector[i])

	return finalvalue


def printmatrix(m):
	for i in range(len(m)):
		print(m[i], hex(gf.value(m[i])))
