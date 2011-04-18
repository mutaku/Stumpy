#!/usr/bin/env python
import string
from random import choice

key = ""
for x in [choice(string.letters+string.digits+string.punctuation) for y in range (50)]:
	key += x
print
print "Here is your key. Copy the following and use for SECRET_KEY in local_settings.py."
print
print key
print
print
