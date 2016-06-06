#!/usr/bin/python
# PIXELSTURM - FreeDNS IPv6 Updater V1

import urllib2
import os.path
 
OLDIP_FILE = '/var/lib/misc/oldipv6'
 
def updatedns(ip):
    print urllib2.urlopen("https://freedns.afraid.org/dynamic/update.php?"+url).read().strip()
    f = open(OLDIP_FILE, 'w')
    f.write(ip)
    f.close()

reg = "your-direct-update-url"
newip = urllib2.urlopen("https://any-service-for-current-ip").read().strip()
url = reg+"&address="+newip

if not os.path.exists(OLDIP_FILE):
    updatedns(newip)
else:
    f = open(OLDIP_FILE, 'r')
    oldip = f.read()
    f.close()
    if oldip != newip:
        updatedns(newip)
