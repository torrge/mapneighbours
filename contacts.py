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



