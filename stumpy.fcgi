#!/usr/bin/env python
import sys, os

sys.path.insert(0, "..")

os.environ['PYTHON_EGG_CACHE'] = "/tmp/"

os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(["method=threaded", "daemonize=false", "debug=1"])

 
