# Imports
from scapy.all import *


# Parameters
dns_source = "local-ip"                 # IP of that interface
dns_destination = ["ip1","ip2","ip3"]   # List of DNS Server IPs

time_to_live = 128                                                                  
query_name = "exampe.com"                                                          
query_type = ["ANY", "A","AAAA","CNAME","MX","NS","PTR","CERT","SRV","TXT", "SOA"] 


for i in range(0,len(query_type)):
    for j in range(0, len(dns_destination)):

        p= IP(src=dns_source, dst=dns_destination[j], ttl=time_to_live) / UDP() / DNS(rd=1, qd=DNSQR(qname=query_name, qtype=query_type[i]))
        
        # Sending the packet

        query = sr1(p,verbose=False, timeout=8)
