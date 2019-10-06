# AES algorithm (128-bit) with Python

This is a slow implementation of Advanced Encryption Standard algorithm. The implementation is by no means secure,
and some of the mechanics were done with visualization in mind rather than efficiency.

However, the code constructs the AES substitution boxes instead using ready made boxes. The mathematics constructing 
sboxes is rather complex, and this might open opportunities to tweak those (probably breaking security further).

