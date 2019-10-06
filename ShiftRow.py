import gf


# This actually changes column major mode?!?!
# row major to column major / vice versa

def do(state):

	r0, r1, r2, r3 = bytearray(), bytearray(), bytearray(), bytearray()

	for i in range(4):

		r0.append(state[i * 4])
		r1.append(state[1 + i * 4])
		r2.append(state[2 + i * 4])
		r3.append(state[3 + i * 4])

	r1 = gf.circrotateleft(r1)
	r2 = gf.circrotateleft(gf.circrotateleft(r2))
	r3 = gf.circrotateright(r3)

	newstatematrix = r0 + r1 + r2 + r3

	return newstatematrix


def inverse(state):

	r0, r1, r2, r3 = bytearray(), bytearray(), bytearray(), bytearray()

	for i in range(4):
		r0.append(state[i * 4])
		r1.append(state[1 + i * 4])
		r2.append(state[2 + i * 4])
		r3.append(state[3 + i * 4])

	r1 = gf.circrotateright(r1)
	r2 = gf.circrotateleft(gf.circrotateleft(r2))
	r3 = gf.circrotateleft(r3)

	newstatematrix = changematrixmode(r0 + r1 + r2 + r3)

	#changematrixmode(newstatematrix)

	return newstatematrix


def changematrixmode(state):
	r0, r1, r2, r3 = bytearray(), bytearray(), bytearray(), bytearray()

	for i in range(4):
		r0.append(state[i * 4])
		r1.append(state[1 + i * 4])
		r2.append(state[2 + i * 4])
		r3.append(state[3 + i * 4])

	newstatematrix = r0 + r1 + r2 + r3

	return newstatematrix
