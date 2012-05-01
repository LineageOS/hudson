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
    patch_count = 0
    junk = number[len(number) - 2:]

    while 0 != os.system('cd %s ; git fetch http://review.cyanogenmod.com/%s refs/changes/%s/%s/%s' % (project, data['project'], junk, number, patch_count + 1)):
        patch_count = patch_count + 1

    while 0 == os.system('cd %s ; git fetch http://review.cyanogenmod.com/%s refs/changes/%s/%s/%s' % (project, data['project'], junk, number, patch_count + 1)):
        patch_count = patch_count + 1

    os.system('cd %s ; git fetch http://review.cyanogenmod.com/%s refs/changes/%s/%s/%s' % (project, data['project'], junk, number, patch_count))
    os.system('cd %s ; git merge FETCH_HEAD' % project)