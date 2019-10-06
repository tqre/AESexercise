def do(state, roundkeys, round):

	statematrix = bytearray()
	
	for i in range(16):

		statematrix.append(state[i] ^ roundkeys[round][i])

	return statematrix


