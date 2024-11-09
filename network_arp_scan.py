from scapy.all import *
import sys

if len(sys.argv) < 3 or sys.argv[1] in ("-h","help","h",""):
        print("usage: python3 network_arp_scan.py 10.10.x.x(ip_block) 24(mask)")
else:
        interface = "eth0"
        ip_range = "{sys.argv[1]}/{sys.argv[2]}"
        broadcastMac = "ff:ff:ff:ff:ff:ff"

        packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)             #ethernet request with broadcast mac add with chained arp determining ips
        ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)  #ans(touple) = sent,recived_packet | , to distribute touple values | unans = no response

        for send,receive in ans:
                print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))


