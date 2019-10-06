import gf


def maketable():

	rcontable = []
	rcontable.append([1, 0, 0, 0, 1, 1, 0, 1])  # rcon[0]

	rcon = gf.makeblist(0x01)
	rijn = gf.makeblist(0x11b)

	for i in range(52):
		rcontable.append(rcon)
		# this is actually a leftwise shift, multiply by 2
		rcon = gf.mul(rcon, [0, 0, 0, 0, 0, 0, 1, 0])
		if gf.value(rcon) > 255:
			# take the remainder from division operation (modulus)
			rcon = gf.div(rcon, rijn)[1]

	return rcontable
