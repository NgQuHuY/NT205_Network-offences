import sys
from scapy.all import *

topt = [('Timestamp',(10,0))]

p = IP(dst='IP', id =1111, ttl=99)/TCP(sport=RandShort(),dport=[22.80], seq=12345,ack=1000,window=1000,flag="S",option=topt)

ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)

ans.sumary()
unans.sumary()