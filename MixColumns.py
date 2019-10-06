# AES 128bit MixColumns
import gf


def do(state):

	fixedmatrix = bytearray([0x02, 0x03, 0x01, 0x01])

	c0, c1, c2, c3 = bytearray(), bytearray(), bytearray(), bytearray()

	# forward ShiftRows still changes matrix mode...
	for i in range(4):
		c0.append(state[i * 4])
		c1.append(state[1 + i * 4])
		c2.append(state[2 + i * 4])
		c3.append(state[3 + i * 4])

	newstatematrix = mix(c0) + mix(c1) + mix(c2) + mix(c3)

	return newstatematrix


def inverse(m):
	# put variables here, and make mix+inv functions one
	fixedmatrix = bytearray([0x0e, 0x0b, 0x0d, 0x09])

	return inv(m[:4]) + inv(m[4:8]) + inv(m[8:12]) + inv(m[-4:])


def mix(column):

	fixedmatrix = bytearray([0x02,0x03,0x01,0x01])
	mixcolumnmatrix = bytearray()

	for i in range(4):

		resultinglist = []
		rijndael = gf.makeblist(0x11b)

		for j in range(4):

			fixedbytelist = gf.makeblist(fixedmatrix[j])
			columnvector = gf.makeblist(column[j])

			resultingbyte = gf.mul(fixedbytelist, columnvector)

			if gf.value(resultingbyte) > 255:
				resultingbyte = gf.div(resultingbyte, rijndael)[1]

			resultinglist.append(resultingbyte)

		finalvalue = gf.add(resultinglist[0], resultinglist[1])
		finalvalue = gf.add(finalvalue, resultinglist[2])
		finalvalue = gf.add(finalvalue, resultinglist[3])

		mixcolumnmatrix.append(gf.value(finalvalue))
		fixedmatrix = gf.circrotateright(fixedmatrix)

	return mixcolumnmatrix


def inv(column):

	fixedmatrix = bytearray([0x0e, 0x0b, 0x0d, 0x09])
	mixcolumnmatrix = bytearray()

	for i in range(0, 4):

		resultinglist = []
		rijndael = gf.makeblist(0x11b)

		for j in range(0, 4):

			fixedbitlist = gf.makeblist(fixedmatrix[j])
			columnvector = gf.makeblist(column[j])

			resultingbyte = gf.mul(fixedbitlist, columnvector)

			while gf.value(resultingbyte) > 255:
				# note the inverted division function!
				resultingbyte = gf.div(rijndael, resultingbyte)[1]

			resultinglist.append(resultingbyte)

		finalvalue = gf.add(resultinglist[0], resultinglist[1])
		finalvalue = gf.add(finalvalue, resultinglist[2])
		finalvalue = gf.add(finalvalue, resultinglist[3])

		mixcolumnmatrix.append(gf.value(finalvalue))

		fixedmatrix = gf.circrotateright(fixedmatrix)

	return mixcolumnmatrix


def blhex(bitlist):
	print(hex(gf.value(bitlist)))
