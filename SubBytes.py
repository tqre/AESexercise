def do(state,sbox):

	newstatematrix = bytearray()

	for i in range(0,16):

		newstatematrix += sbox[state[i]]

	return newstatematrix
