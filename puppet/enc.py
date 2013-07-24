#!/usr/bin/env python
# -*- coding:utf-8 -*-

import yaml
import urllib2
import os
import sys
import json

JSON_CACHE = '/var/tmp/api-cache.json'

def getHosts():
    url = "http://127.0.0.1:8000/api/gethosts.json"
    try:
        data = urllib2.urlopen(url).read()
        writeFile(JSON_CACHE,data)
    except:
        data = open(JSON_CACHE,'r').read()
    return json.loads(data)

def writeFile(f,s):
    with open(f,'w') as fd:
        fd.write(s)

def getHostClass(data, hostname):
    ret = set()
    for hostgroup in data:
        if hostname in [h['hostname'] for h in hostgroup['members']]:
            ret.add(str(hostgroup['hostgroup']))
    return ret

def main():
    cmdb_data = getHosts()
    #print cmdb_data
    if cmdb_data['status'] == 0:
        classes = getHostClass(cmdb_data['data'],sys.argv[1])
        data = {'classes':list(classes)}
    enc = yaml.dump(data,explicit_start=True,default_flow_style=False)
    print enc
    #print classes

if __name__ == '__main__':
    main()
