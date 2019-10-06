# AES algorithm (128-bit, ECB mode) with Python

The project was insipired by cryptopals.com challenges, and was mainly done as an exercise to learn Python.

This is a slow and bulky implementation of Advanced Encryption Standard algorithm. The implementation is by no means secure,
and some of the mechanics were done with visualization in mind rather than efficiency.

However, the code constructs the AES substitution boxes instead using ready made boxes. The mathematics constructing 
sboxes are rather complex, and understanding them might open opportunities to tweak those (probably breaking security further).

https://www.cryptopals.com/

Last changes have been made around October 2018, and the project is not worked on anymore.
