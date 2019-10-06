# AES algorithm (128-bit, ECB mode) with Python

The project was insipired by cryptopals.com challenges, and was mainly done as an exercise to learn Python.

This is a slow and bulky implementation of the Advanced Encryption Standard algorithm. The implementation is by no means secure,
and some of the mechanics were done with visualization in mind rather than efficiency. The code works with ECB mode, but a
CBC conversion is just a matter of xorring initialization vectors appropriately on the right spot ;)

However, the code constructs the AES substitution boxes instead using ready made boxes. The mathematics constructing 
sboxes are rather complex, including Galois' Field equations and affine transformations, and tweaking them might open opportunities to customize the whole algorithm (most likely breaking the security further without proper analysis).

https://www.cryptopals.com/

Last changes have been made around October 2018, and the project is not worked on anymore.
