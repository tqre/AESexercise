# AES decryption algorithm for 128-bit key + 128-bit block size
import sbox, MixColumns, SubBytes, ShiftRow, roundkeys, AddRoundKey


def do(key, ciphertext):

	key = key.encode()
	statematrix = bytes.fromhex(ciphertext)

	# inverse sbox generation
	subbox = sbox.makeinverse()

	# Initial decryption round:
	allkeys = roundkeys.makeall(key)
	rnd = 10
	statematrix = AddRoundKey.do(statematrix, allkeys, rnd)
	statematrix = ShiftRow.inverse(statematrix)
	statematrix = SubBytes.do(statematrix, subbox)

	for i in range(9):
		rnd -= 1
		statematrix = AddRoundKey.do(statematrix, allkeys, rnd)
		statematrix = MixColumns.inverse(statematrix)
		statematrix = ShiftRow.inverse(statematrix)
		statematrix = SubBytes.do(statematrix, subbox)

	# Last Round:
	rnd = 0
	statematrix = AddRoundKey.do(statematrix, allkeys, rnd)

	# Plaintext: (UTF-8 decoded)
	# Maybe return byte-type object here?
	return statematrix
