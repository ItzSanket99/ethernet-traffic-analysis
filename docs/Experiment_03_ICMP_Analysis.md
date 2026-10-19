# Experiment 3: ICMP Traffic Analysis

## Aim
Capture and analyse ICMP Echo Request and Echo Reply packets.

## Environment
- Operating system: Pop!_OS 24.04 LTS
- Interface: wlp4s0
- Destination: 10.199.50.47

## Procedure
1. Start packet capture using dumpcap.
2. Generate four ICMP requests using ping.
3. Save the capture as wireshark/icmp_capture.pcapng.
4. Inspect packets in Wireshark using the filter `icmp`.

## Packet Fields
Record the source IP, destination IP, ICMP type, sequence number,
and IPv4 TTL from the captured packets.

## Observations
Complete this section using the actual packet capture and ping output.

## Conclusion
ICMP Echo Requests and Echo Replies can be used to investigate
IP reachability and measure round-trip time. A successful reply
indicates that the destination responded to the request.
