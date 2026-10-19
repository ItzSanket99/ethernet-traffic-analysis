# Experiment 4: TCP Traffic Analysis

## Aim
Capture TCP traffic and investigate connection establishment,
port numbers, TCP flags, and data transfer.

## Environment
- Operating system: Pop!_OS 24.04 LTS
- Interface: wlp4s0
- Test application: curl using HTTPS

## Procedure
1. Capture TCP packets using dumpcap.
2. Generate an HTTPS request using curl.
3. Open the saved capture in Wireshark.
4. Apply the display filter `tcp`.
5. Identify the three-way handshake and subsequent data segments.

## Fields to Record
- Source and destination IP addresses
- Source and destination TCP ports
- SYN and ACK flags
- Sequence and acknowledgment numbers
- TCP payload length

## Observations
Record the actual packet fields from the capture.
Do not assume that every TCP connection uses the same port numbers.

## Conclusion
TCP establishes connections using a handshake and provides
reliable, ordered delivery of application data.
