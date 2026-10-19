# Experiment 2: ARP Protocol Analysis

## Aim
Investigate ARP requests, replies, and IPv4-to-MAC address resolution.

## Environment
- OS: Pop!_OS 24.04 LTS
- Interface: wlp4s0
- Local IPv4: 10.199.50.243
- Gateway IPv4: 10.199.50.47

## Tools
- ip neigh
- ping
- dumpcap
- tshark
- Wireshark

## Procedure
1. Identified the default gateway and active interface.
2. Removed the cached gateway neighbor entry.
3. Generated traffic to the gateway.
4. Captured ARP traffic.
5. Inspected packet fields.

## Observations
The terminal capture showed an ARP request for 10.199.50.47
from 10.199.50.243 and a reply mapping the gateway to
da:c4:d6:26:cf:6f.

The local MAC address observed was d8:c0:a6:58:b8:a5.

## Conclusion
The observed ARP exchange demonstrates how a host discovers
the link-layer address associated with a local IPv4 destination.
