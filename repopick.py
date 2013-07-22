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
    f = urllib.request.urlopen('http://review.cyanogenmod.org/query?q=change:%s' % change)
    d = f.read().decode()
    # gerrit doesnt actually return json. returns two json blobs, separate lines. bizarre.
    print(d)
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

    print(project)
    number = data['number']
    patch_count = 0
    junk = number[len(number) - 2:]

    if not os.path.isdir(project):
        sys.stderr.write('no project directory: %s' % project)
        sys.exit(1)

    while 0 != os.system('cd %s ; git fetch http://review.cyanogenmod.org/%s refs/changes/%s/%s/%s' % (project, data['project'], junk, number, patch_count + 1)):
        patch_count = patch_count + 1

    while 0 == os.system('cd %s ; git fetch http://review.cyanogenmod.org/%s refs/changes/%s/%s/%s' % (project, data['project'], junk, number, patch_count + 1)):
        patch_count = patch_count + 1

    os.system('cd %s ; git fetch http://review.cyanogenmod.org/%s refs/changes/%s/%s/%s' % (project, data['project'], junk, number, patch_count))
    os.system('cd %s ; git merge FETCH_HEAD' % project)
