import sys
import urllib
import urllib2
import json
import os
import subprocess
import re

for change in sys.argv[1:]:
    print change
    f = urllib2.urlopen('http://review.cyanogenmod.com/query?q=change:%s' % change)
    d = f.read()
    # gerrit doesnt actually return json. returns two json blobs, separate lines. bizarre.
    d = d.split('\n')[0]
    data = json.loads(d)
    project = data['project']
    plist = subprocess.Popen([os.environ['HOME']+"/bin/repo","list"], stdout=subprocess.PIPE)
    while(True):
        retcode = plist.poll()
        pline = plist.stdout.readline().rstrip()
        ppaths = re.split('\s*:\s*',pline)
        if ppaths[1] == project:
            project = ppaths[0]
            break
        if(retcode is not None):
            break

    retval = os.system('cd %s ; xmllint --noout `git show FETCH_HEAD | grep "^+++ b"  | sed -e \'s/^+++ b\///g\' | egrep "res/.*xml$"`' % (project))
    sys.exit(retval!=0)
