# AES Algorithm, generating 128bit roundkeys
import sbox, gf, rcon


def makeroundkey(previouskey, round, rcontable, subbox):

	# Split the key to 4 byte slices:
	w0 = bytearray(previouskey[0:4])
	w1 = bytearray(previouskey[4:8])
	w2 = bytearray(previouskey[8:12])
	w3 = bytearray(previouskey[-4:])

	# Perform a circular byte left shift to w3: [0,1,2,3] -> [1,2,3,0]
	gw3 = bytearray(w3[1:] + w3[:1])

	# Apply Rijndael S-box to gw3 bytes (substitution):

	for i in range(len(gw3)):
		gw3[i] = int.from_bytes(subbox[gw3[i]], byteorder='big')

	# Add round constant to the leftmost byte in gw3
	# Adding is in GF

	rconbyte = gf.makeblist(gw3[0])
	gw3[0] = gf.value(gf.add(rcontable[round], rconbyte))

	# Build the roundkey:

	w4 = bytearray(4)
	w5 = bytearray(4)
	w6 = bytearray(4)
	w7 = bytearray(4)

	for i in range(4):
		w4[i] = gw3[i] ^ w0[i]

	for i in range(4):
		w5[i] = w4[i] ^ w1[i]

	for i in range(4):
		w6[i] = w5[i] ^ w2[i]

	for i in range(4):
		w7[i] = w6[i] ^ w3[i]

	roundkey = w4 + w5 + w6 + w7

	return roundkey


def makeall(secretkey):

	rcontable = rcon.maketable()
	subbox = sbox.make()
	roundkeys = []

	# initial key is same as the original key
	roundkeys.append(secretkey)

	# makes a bytearray of 10 first keys,
	for i in range(1,11):

		roundkeys.append(makeroundkey(secretkey, i, rcontable, subbox))
		secretkey = makeroundkey(secretkey, i, rcontable, subbox)

	# for 192 or 256-bit versions, more keys are needed

	return roundkeys


def printroundkeys(secretkey):

	roundkeys = makeall(secretkey)

	for i in range(len(roundkeys)):
		print("Round", [i], roundkeys[i])

	for i in range(len(roundkeys)):
		print("Round", [i], roundkeys[i].hex())


