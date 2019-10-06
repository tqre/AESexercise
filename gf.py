# Galois field arithmetics:
# Uses lists [0,0,0,0,0,0,0,0] for handling bits in bytes


# This function actually accepts bytes too!
def makeblist(hexvalue):
	bitlist = []
	conversionvalue = 256
	for i in range(9):
		bitlist.append(hexvalue // conversionvalue)
		if hexvalue >= conversionvalue:
			hexvalue -= conversionvalue
		conversionvalue //= 2
	return bitlist


def removeleadingzeros(bitlist):
	try:
		while bitlist[0] == 0:
			bitlist.remove(0)
	except:
		pass


def removeleadingzero(bitlist):
	if bitlist[0] == 0:
		bitlist.pop(0)
	return bitlist


def addtrailingzeros(bitlist, number):
	for i in range(number):
		bitlist.append(0)
	return bitlist


def addleadingzeros(bitlist, number):
	for i in range(number):
		bitlist.insert(0, 0)


def circrotateright(bitlist):
	return bitlist[-1:] + bitlist[:-1]


def circrotateleft(bitlist):
	return bitlist[1:] + bitlist[:1]


def value(bitlist):

	decvalue = 0
	for i in range(len(bitlist)):
		decvalue += 2 ** i * bitlist[-i - 1]

	return decvalue


def add(a, b):
	# addition and subtraction is the same: xor
	# need to take care that bitlists are of same length

	sumvalue = []
	while len(a) < len(b):
		addleadingzeros(a, 1)
	while len(b) < len(a):
		addleadingzeros(b, 1)

	for i in range(len(a)):
		sumvalue.append(a[i] ^ b[i])

	return sumvalue


def div(dividend, divisor):

	removeleadingzeros(dividend)
	removeleadingzeros(divisor)
	quotient = [0,0,0,0,0,0,0,0]

	while True:

		remainder = []
		quotient[-(len(divisor) - len(dividend) +1)] = 1

		for i in range(len(divisor)):
			try:
				remainder.append(dividend[i] ^ divisor[i])
			except:
				remainder.append(divisor[i])

		removeleadingzeros(remainder)
		divisor = remainder

		if value(remainder) < value(dividend):
			break

	removeleadingzeros(quotient)
	return [quotient, remainder]


def mul(a, b):

	product = [0,0,0,0,0,0,0,0]
	removeleadingzeros(a)

	for i in range(len(a)):

		if a[-i - 1] == 1:
			product = add(product, b)

		addtrailingzeros(b, 1)
		removeleadingzero(b)

	return product


def inverse(t):
	# This is the Extended Euclidean algorithm in GF(2⁸)

	r1 = makeblist(int("0x11b",16))
	r2 = t
	aux1 = [0]
	aux2 = [1]

	if value(t) == 1:
		return [0,0,0,0,0,0,0,1]

	if value(t) == 0:
		return [0,0,0,0,0,0,0,0]

	while True:
		q = div(r2, r1)[0]
		r1, r2 = r2[:], div(r2, r1)[1]
		aux1, aux2 = aux2, add(aux1, mul(aux2, q))

		if value(r2) == 1:
			break

	return aux2
