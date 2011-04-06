#!/usr/bin/env python


class Encode():
	"""
	Encode a number to Base62 using master string
		base62.Encode(12).string will result in string "b"
		encoded_string = base62.Encode(4).string
	"""
	def __init__(self,num):
		self.num = num
		self.master = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.make_encode()
	def make_encode(self):
		self.string = ""
		if (self.num == 0):
			self.string = self.master[0]
		self.build_string = []
		self.base = len(self.master)
		while self.num:
			rem = self.num % self.base
			self.num = self.num // self.base
			self.build_string.append(self.master[rem])
		self.build_string.reverse()
		self.string = ''.join(self.build_string)

class Decode():
	"""
	Decode a base62 encoded string to a number
		base62.Decode("b").num will result in integer 12
		decoded_int = base62.Decode("3D").num
	"""
	def __init__(self,string):
		self.string = string	
		self.master = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.make_decode()
	def make_decode(self):
		self.base = len(self.master)
		self.string_length = len(self.string)
		self.num = 0
		self.i = 0
		for char in self.string:
			pow = (self.string_length - (self.i + 1))
			self.num += self.master.index(char) * (self.base ** pow)
			self.i += 1
