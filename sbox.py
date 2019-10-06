import gf, aff


def make():

	table = []
	for i in range(0, 256):
		bitlist = gf.makeblist(int(i))
		table.append(gf.inverse(bitlist))

	affmatrix = aff.makematrix()
	sbox = []

	for i in range(0, 256):
		sbox.append(aff.transform(table[i], affmatrix))

	for i in range(0, 256):
		sbox[i] = bytes([gf.value(sbox[i])])

	return sbox


def makeinverse():

	sbox = []
	for i in range(0, 256):
		bitlist = gf.makeblist(int(i))
		gf.removeleadingzero(bitlist)
		sbox.append(bitlist)

	affmatrix = aff.makeinversematrix()

	for i in range(0,256):
		sbox[i] = aff.inversetransform(sbox[i], affmatrix)
		sbox[i] = gf.inverse(sbox[i])

	for i in range(0, 256):
		sbox[i] = bytes([gf.value(sbox[i])])

	#aff.printmatrix(sbox)

	return sbox

