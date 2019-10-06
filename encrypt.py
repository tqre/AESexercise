# AES encryption algorithm for 128-bit key + 128-bit block size
import sbox, MixColumns, SubBytes, ShiftRow, roundkeys, AddRoundKey


def do(key, plaintext):

	# add validity checks (128bits blocks)

	key = key.encode()

	try:
		statematrix = plaintext.encode()
	except AttributeError:
		statematrix = plaintext

	# Generate forward sbox
	subbox = sbox.make()

	# Make roundkeys from key (10 for 128bit AES)
	allkeys = roundkeys.makeall(key)
	rnd = 0

	for r in range(9):
		statematrix = AddRoundKey.do(statematrix, allkeys, rnd)
		statematrix = SubBytes.do(statematrix, subbox)
		statematrix = ShiftRow.do(statematrix)
		statematrix = MixColumns.do(statematrix)
		rnd += 1

	# Final round:
	statematrix = AddRoundKey.do(statematrix, allkeys, rnd)
	statematrix = SubBytes.do(statematrix, subbox)
	statematrix = ShiftRow.do(statematrix)

	# without mixcolumns changing matrix mode in the final round
	# we have to do it here
	statematrix = ShiftRow.changematrixmode(statematrix)
	rnd += 1
	statematrix = AddRoundKey.do(statematrix, allkeys, rnd)

	# Ciphertext:

	return statematrix.hex()
