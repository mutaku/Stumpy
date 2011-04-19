#!/usr/bin/env python
import string
from random import sample

AVAIL_CHARS = string.digits+string.letters+string.punctuation.replace("'","").replace('"',"").replace("\\","")

print
print "Here is your key. Copy the following and use for SECRET_KEY in local_settings.py."
print
print "Key ==> ",''.join(sample(AVAIL_CHARS,50))
print
