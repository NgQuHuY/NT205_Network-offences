import sys
from scapy.all import *

dstIP = ''

send(fragment(IP(dst=dstIP)/ICMP())/('X'*60000))