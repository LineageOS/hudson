import sys
import urllib
import urllib2
import json
import os

for change in sys.argv[1:]:
    print change
    f = urllib2.urlopen('http://review.cyanogenmod.com/query?q=change:%s' % change)
    d = f.read()
    # gerrit doesnt actually return json. returns two json blobs, separate lines. bizarre.
    print d
    d = d.split('\n')[0]
    data = json.loads(d)
    project = data['project']
    project = project.replace('CyanogenMod/', '').replace('android_', '')

    while not os.path.isdir(project):
        new_project = project.replace('_', '/', 1)
        if new_project == project:
            break
        project = new_project

    print project
    number = data['number']
    os.system('cd %s ; CURRENT_HEAD=$(git rev-list HEAD --max-count 1) ; repo download . %s ; git merge $CURRENT_HEAD' % (project, number))
