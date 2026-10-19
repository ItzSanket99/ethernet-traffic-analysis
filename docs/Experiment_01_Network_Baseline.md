# Experiment 1: Network Interface and Addressing Investigation

## Aim
To inspect Linux network interfaces, assigned IP addresses, routing
configuration, and basic IPv4 connectivity.

## Environment
- Operating system: Pop!_OS 24.04 LTS
- Platform: Linux

## Commands
1. `ip addr`
2. `ip route`
3. `hostname -I`
4. `ping -c 4 1.1.1.1`

## Observations
Refer to `results/network_baseline.txt` for the actual command outputs.

## Analysis
- `ip addr` displays interfaces, link-layer addresses, and assigned IP addresses.
- `ip route` displays routing entries and the default gateway, if configured.
- `hostname -I` displays host IP addresses.
- `ping` tests reachability using ICMP Echo Requests and Echo Replies.

## Conclusion
The network configuration and connectivity results will be evaluated
using the captured command outputs. Conclusions must reflect the
observed results.
