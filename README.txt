  //////////////////////////////////////////
 /// FRAGGLE ATTACK - DENIAL-OF-SERVICE ///
//////////////////////////////////////////

What is a Fraggle Attack?
    A 'Fraggle Attack' is an Amplified Denial-of-Service attack that mostly occurs over an
    individual's local network (this is generally because most perimeter routers are configured
    not to forward any external traffic that is directed to their broadcast address).

How it works?
    The attacker crafts spoofed UDP packets which are sent to the Broadcast Address of the
    network (for example: 192.168.1.255). Each source-address of the packet is spoofed to be
    the source-address belonging to the local machine that the attacker wants to bring down.

    Generally, port 7 (Echo) or port 19 (CharGen) are used. The idea is that there are other
    devices on the network that respond to UDP traffic on these ports. The attacker sends
    spoofed UDP packets to the broadcast address, the traffic then gets forwarded to the
    other local devices on the network, and finally they all respond to the traffic.

    The traffic ends up landing at the endpoint of the target. The target will be under heavy
    load and will ultimately succumb to a Denial-of-Service attack.

Requirements?
    - Latest SCAPY library (pip3 install scapy)

    - Root elevation and a BASH shell


  Have fun :)
