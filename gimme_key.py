#!/usr/bin/env python
import string
from random import sample

print
print "Here is your key. Copy the following and use for SECRET_KEY in local_settings.py."
print
print "Key ==> ",''.join(sample(string.letters+string.digits+string.punctuation,50))
print
