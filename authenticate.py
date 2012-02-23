#!/usr/bin/env python

import sys
import urllib2
import urllib
import os
import json

username = os.getenv('U')
password = os.getenv('P')

# will throw if it fails
result = json.loads(urllib2.urlopen('https://github.com/api/v2/json/user/show/%s?login=%s&token=%s' % (username, username, password)).read())

orgs = json.loads(urllib2.urlopen('https://github.com/api/v2/json/user/show/%s/organizations' % username).read())

for org in orgs.get('organizations'):
  if org.get('login') == 'CyanogenMod':
    print "success"
    sys.exit(0)

print "not a member of org"
sys.exit(1)
