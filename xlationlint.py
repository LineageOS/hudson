#!/usr/bin/env python

import sys
import json
import os
import subprocess
import re

try:
  # For python3
  import urllib.request
except ImportError:
  # For python2
  import imp
  import urllib2
  urllib = imp.new_module('urllib')
  urllib.request = urllib2

for change in sys.argv[1:]:
    print(change)
    f = urllib.request.urlopen('http://review.cyanogenmod.com/query?q=change:%s' % change)
    d = f.read().decode()
    # gerrit doesnt actually return json. returns two json blobs, separate lines. bizarre.
    d = d.split('\n')[0]
    data = json.loads(d)
    project = data['project']
    plist = subprocess.Popen([os.environ['HOME']+"/bin/repo","list"], stdout=subprocess.PIPE)
    while(True):
        retcode = plist.poll()
        pline = plist.stdout.readline().rstrip()
        ppaths = re.split('\s*:\s*', pline.decode())
        if ppaths[1] == project:
            project = ppaths[0]
            break
        if(retcode is not None):
            break

    retval = os.system('cd %s ; xmllint --noout `git show FETCH_HEAD | grep "^+++ b"  | sed -e \'s/^+++ b\///g\' | egrep "res/.*xml$"`' % (project))
    sys.exit(retval!=0)
