# -*- coding: utf-8 -*-
# Copyright (C) 2013 Juntao ZH<zjuntor@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import urllib2
import xml.dom.minidom as minidom

__all__ = ['getUserNeighbours']

apikey = '0e85d17cb0c7871c2b91747612569554'
contactsURLPattern = 'http://api.douban.com/people/%s/contacts?max-results=%s&apikey=%s'
maxResults = '1000'

def buildURL(uid,max_results,apikey):
    return contactsURLPattern % (uid,max_results,apikey)


def extractUsersInfo(xml):
    usersInfo = {}
    
    dom = minidom.parseString(xml)
    users = dom.getElementsByTagName('entry')
    
    for user in users:
        name = user.getElementsByTagName('title')[0].childNodes[0].data
        try:
            location = user.getElementsByTagName('db:location')[0].childNodes[0].data
        except:
            location = ''
        try:
            avatar = user.getElementsByTagName('link')[2].getAttribute('href')
        except:
            avatar = ''
        try:
            signature = user.getElementsByTagName('db:signature')[0].childNodes[0].data
        except:
            signature = ''
        usersInfo[name] = {'name':name,'location':location,'avatar':avatar,'signature':signature}

    return usersInfo

def getUserNeighbours(uid):
    return extractUsersInfo(urllib2.urlopen(buildURL(uid,maxResults,apikey)).read())



