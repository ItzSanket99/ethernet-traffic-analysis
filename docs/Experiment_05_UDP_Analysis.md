# Experiment 5: UDP Traffic Analysis

## Aim
Investigate UDP ports, payload transfer, and connectionless communication.

## Environment
- Operating system: Pop!_OS 24.04 LTS
- Capture interface: lo
- Server address: 127.0.0.1
- Server port: 5005

## Procedure
1. Start the Python UDP server.
2. Send a message using the UDP client.
3. Capture UDP traffic using dumpcap.
4. Inspect the packets in Wireshark using `udp.port == 5005`.

## Observations
Record the actual source and destination ports, packet lengths,
and payload contents from the capture.

## Analysis
UDP transfers datagrams without a TCP-style connection handshake.
It does not guarantee delivery, ordering, or retransmission.
An application may implement its own reliability mechanisms.

## Conclusion
The captured client-server exchange demonstrates UDP datagram
transmission and reception over the local loopback interface.
