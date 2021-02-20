# Cybersecurity

# Caesar Cipher Decrypter



![cybersecurity-looks-to-the-cloud-to-protect-data-at-sea](https://user-images.githubusercontent.com/75733364/108591332-42e84280-738e-11eb-9cd8-cbc3090f4394.jpg)



The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.
Thus to cipher a given text we need an integer value, known as shift which indicates the number of position each letter of the text has been moved down.
The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described mathematically as.

- ![image](https://user-images.githubusercontent.com/75733364/108591645-cd7d7180-738f-11eb-8e0b-31f04f6684e7.png)

- ![image](https://user-images.githubusercontent.com/75733364/108591658-da9a6080-738f-11eb-816b-4d1c3d442ab6.png)

![ceaserCipher](https://user-images.githubusercontent.com/75733364/108591674-e6862280-738f-11eb-801e-f7917d563982.png)

- Caesar Cipher falls under the category of monoalphabetic type of substitution, because the replacement remains the same throughout the message.
- It is a symmetric type of encryption technique, because a symmetric encryption is a kind of technique where the same key is used to both encrypt as well as decrypt the data. 

# Steps for designing and using a Caesar cipher

- Choose a value to shift the alphabet by.

- Make a table where the top row contains letters in standard alphabetical order, and the bottom row is the new shifted alphabet.

- Encode the message by exchanging each letter in the message with the equivalent shifted letter.

- Make sure that the message’s intended recipient knows the shifting scheme you used to encode the message so they can decode it.

- To decrypt a message encoded with a Caesar cipher, simply take the value of 26 minus the shift value, and apply that new value to shift the encoded message back to its original form.

# Row :

# a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j

# Note : This is a shift of 10.

For eg.

- Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ
- Shift: 10
- Cipher: KLMNOPQRSTUVWXYZABCDEFGHIJ

- Text : ATTACKATONCE
- Shift: 4
- Cipher: EXXEGOEXSRGI


# How a Caesar Cipher Decrypter Works?
We can either write another function decrypt similar to encrypt, that’ll apply the given shift in the opposite direction to decrypt the original text. However we can use the cyclic property of the cipher under modulo , hence we can simply observe

- Cipher(n) = De-cipher(26-n)

Hence, we can use the same function to decrypt, instead we’ll modify the shift value such that shift = 26-shift .

# Pros and Cons of a Caesar Cipher :

A Caesar cipher is very easy to design, but also very easy to decode. To crack a Caesar code, a decoder could simply go through every possible shift of the alphabet (all 26 of them) and see if any sensible message appears. This is a relatively small number of combinations to check, for perspective, a message encoded with a Vigenère cipher has over 11 million possible combinations (and that is if the key is only five letters long — the longer the key, the more combinations), and the Enigma code has 158,962,555,217,826,360,000  possible combinations.

