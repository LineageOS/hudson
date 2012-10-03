#!/usr/bin/python2

import httplib
import json
import os
import re
import sys

if len(sys.argv) != 2:
  print "You done goofed! This takes exactly one argument: the device lunch combo"
  sys.exit(1)

device = sys.argv[1]
device = re.sub('^cm_','',device,1)
device = re.sub('-[^-]*$','',device,1)

if len(device) <= 0:
  print "No device left after parsing input?"
  sys.exit(2)

if 'CM_RELEASE' in os.environ:
  channel = 'stable'
  limit = 1
elif 'CM_NIGHTLY' in os.environ:
  channel = 'nightly'
  limit = 5
else:
  sys.exit(3)

if limit > 1:
  logrequest = '{"method": "get_all_builds", "params":{"device":"%s", "channels": ["%s"], "limit": "%d"}}' % (device, channel, limit)
else:
  logrequest = '{"method": "get_builds", "params":{"device":"%s", "channels": ["%s"]}}' % (device, channel)


headers = {}
headers['Content-Type'] = 'application/json'
headers['User-Agent'] = 'CyanogenMod changelog builder'
headers['Accept'] = '*/*'
headers['Content-Length'] = "%d" % (len(logrequest))

conn = httplib.HTTPConnection('get.cm', 80)
conn.connect()
request = conn.putrequest('POST', '/api')

for k in headers:
    conn.putheader(k, headers[k])
conn.endheaders()

conn.send(logrequest)

resp = conn.getresponse()
jsonreply = json.load(resp)
conn.close()
builds = jsonreply['result']

for build in builds:
  print build['timestamp']

