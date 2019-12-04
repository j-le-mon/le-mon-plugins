from urllib2 import Request, urlopen
from urllib2 import URLError, HTTPError
req = Request('http://192.168.8.246')
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print ('CRITICAL - Serwer nieosiagalny', e.reason)
        raise SystemExit, 3
    elif hasattr(e, 'code'):
        print ('Serwer nie moze wykonac zapytania', e.reason)
        raise SystemExit, 2
else:
    print ('OK - dziala polaczenie do KIR', response.getcode())
    raise SystemExit, 0

